"""
VirusTotal API Integration
Replaces Hybrid Analysis — works immediately with no vetting required.
Checks file against 70+ antivirus engines and returns real threat score.
"""

import requests
import time
import logging
import hashlib

logger = logging.getLogger(__name__)

VT_API_KEY  = "ededfb21a58830371c6eceddbdc0156b0d30eadaf8d82e3edc23251717538839"
VT_BASE_URL = "https://www.virustotal.com/api/v3"


def get_headers():
    return {"x-apikey": VT_API_KEY, "accept": "application/json"}


# ── 1. Hash lookup (instant if file was scanned before) ─────────────────────
def check_hash(sha256: str) -> dict:
    try:
        resp = requests.get(f"{VT_BASE_URL}/files/{sha256}", headers=get_headers(), timeout=20)
        logger.info(f"VT hash lookup: status={resp.status_code}")
        if resp.status_code == 200:
            return {"found": True, "report": resp.json()}
        return {"found": False}
    except Exception as e:
        logger.error(f"VT hash lookup error: {e}")
        return {"found": False}


# ── 2. Upload file ───────────────────────────────────────────────────────────
def upload_file(filepath: str, filename: str) -> dict:
    try:
        file_size = __import__("os").path.getsize(filepath)

        # Files > 32MB need a special upload URL
        if file_size > 32 * 1024 * 1024:
            url_resp = requests.get(f"{VT_BASE_URL}/files/upload_url", headers=get_headers(), timeout=15)
            upload_url = url_resp.json().get("data")
        else:
            upload_url = f"{VT_BASE_URL}/files"

        with open(filepath, "rb") as f:
            resp = requests.post(
                upload_url,
                headers=get_headers(),
                files={"file": (filename, f)},
                timeout=120
            )

        logger.info(f"VT upload: status={resp.status_code}, body={resp.text[:200]}")

        if resp.status_code == 200:
            analysis_id = resp.json().get("data", {}).get("id")
            return {"success": True, "analysis_id": analysis_id}

        return {"success": False, "error": f"Upload failed HTTP {resp.status_code}: {resp.text[:150]}"}

    except Exception as e:
        logger.exception(f"VT upload error: {e}")
        return {"success": False, "error": str(e)}


# ── 3. Poll analysis until complete ─────────────────────────────────────────
def poll_analysis(analysis_id: str, max_wait: int = 120) -> dict:
    url = f"{VT_BASE_URL}/analyses/{analysis_id}"
    elapsed = 0
    interval = 15

    while elapsed < max_wait:
        try:
            resp = requests.get(url, headers=get_headers(), timeout=20)
            logger.info(f"VT poll ({elapsed}s): status={resp.status_code}")

            if resp.status_code == 200:
                data = resp.json()
                status = data.get("data", {}).get("attributes", {}).get("status")
                logger.info(f"VT analysis status: {status}")

                if status == "completed":
                    # Fetch full file report using sha256
                    sha256 = data.get("meta", {}).get("file_info", {}).get("sha256", "")
                    if sha256:
                        file_resp = requests.get(
                            f"{VT_BASE_URL}/files/{sha256}",
                            headers=get_headers(), timeout=20
                        )
                        if file_resp.status_code == 200:
                            return {"success": True, "report": file_resp.json()}
                    # Fallback — return analysis data directly
                    return {"success": True, "report": data}

        except Exception as e:
            logger.error(f"VT poll error: {e}")

        time.sleep(interval)
        elapsed += interval

    return {"success": False, "error": "VirusTotal analysis timed out"}


# ── 4. Parse VT report into your app format ──────────────────────────────────
def parse_vt_report(raw: dict) -> dict:
    # Handle both /files/{sha256} and /analyses/{id} response shapes
    attrs = raw.get("data", {}).get("attributes", {})

    # Stats from last_analysis_stats
    stats = attrs.get("last_analysis_stats") or attrs.get("stats") or {}
    malicious   = stats.get("malicious", 0)   or 0
    suspicious  = stats.get("suspicious", 0)  or 0
    undetected  = stats.get("undetected", 0)  or 0
    harmless    = stats.get("harmless", 0)    or 0
    total       = malicious + suspicious + undetected + harmless
    if total == 0:
        total = 1  # avoid division by zero

    # Threat score out of 100
    threat_score = int(((malicious + suspicious * 0.5) / total) * 100)

    # Label
    if threat_score >= 70 or malicious >= 10:
        label = "Critical"
    elif threat_score >= 40 or malicious >= 5:
        label = "High"
    elif threat_score >= 15 or malicious >= 1:
        label = "Medium"
    else:
        label = "Low"

    # Engine results — collect names of engines that flagged it
    results = attrs.get("last_analysis_results") or attrs.get("results") or {}
    flagged_engines = []
    for engine, result in results.items():
        cat = result.get("category", "")
        res = result.get("result")
        if cat in ["malicious", "suspicious"] and res:
            flagged_engines.append(f"{engine}: {res}")

    # Popular threat label from VT
    popular_threat = ""
    for label_info in (attrs.get("popular_threat_classification") or {}).get("popular_threat_name", []):
        popular_threat = label_info.get("value", "")
        if popular_threat:
            break

    malware_family = (
        attrs.get("popular_threat_classification", {}).get("suggested_threat_label")
        or popular_threat
        or attrs.get("meaningful_name")
        or ""
    )

    # Reasons
    reasons = []
    reasons.append(f"VirusTotal: {malicious} out of {total} antivirus engines flagged this file as malicious")
    if suspicious > 0:
        reasons.append(f"VirusTotal: {suspicious} engines flagged as suspicious")
    if malware_family:
        reasons.append(f"Identified threat label: {malware_family}")
    if flagged_engines:
        top = flagged_engines[:3]
        reasons.append(f"Detections include: {', '.join(top)}")

    # Network / behavior — VT basic doesn't include sandbox, but tags help
    tags = attrs.get("tags") or []
    network_activity = [f"File tag: {t}" for t in tags[:6]]

    # Signatures = flagged engine names (top 8)
    signatures = flagged_engines[:8]

    # Behavior logs
    behavior_logs = []
    if malicious > 0:
        behavior_logs.append({
            "action": "AV Detection",
            "desc": f"Flagged by {malicious} antivirus engines on VirusTotal",
            "severity": label
        })
    if suspicious > 0:
        behavior_logs.append({
            "action": "Suspicious Activity",
            "desc": f"Marked suspicious by {suspicious} engines",
            "severity": "Medium"
        })
    if tags:
        behavior_logs.append({
            "action": "File Properties",
            "desc": f"Tagged as: {', '.join(tags[:4])}",
            "severity": "Medium" if malicious > 0 else "Low"
        })

    return {
        "dynamic_analysis": True,
        "engine": "VirusTotal (70+ AV Engines)",
        "threat_score": threat_score,
        "label": label,
        "verdict": malware_family or ("malicious" if malicious > 0 else "clean"),
        "malware_family": malware_family,
        "av_detect_percent": int((malicious / total) * 100),
        "total_engines": total,
        "malicious_engines": malicious,
        "suspicious_engines": suspicious,
        "signatures": signatures,
        "network_activity": network_activity,
        "processes": [],
        "reasons": reasons,
        "behavior_logs": behavior_logs,
    }


# ── 5. Main entry point ──────────────────────────────────────────────────────
def run_dynamic_analysis(filepath: str, filename: str, sha256: str) -> dict:
    logger.info(f"=== Starting VirusTotal scan for: {filename} ===")

    # Step 1: Hash lookup — instant result if already scanned
    hash_result = check_hash(sha256)
    if hash_result.get("found"):
        logger.info("Found existing VT report via hash lookup")
        return {
            "success": True,
            "data": parse_vt_report(hash_result["report"]),
            "source": "hash_cache"
        }

    # Step 2: Upload fresh file
    logger.info("File not in VT database — uploading fresh...")
    upload = upload_file(filepath, filename)
    if not upload.get("success"):
        return {"success": False, "error": upload.get("error", "Upload failed")}

    analysis_id = upload.get("analysis_id")
    if not analysis_id:
        return {"success": False, "error": "No analysis ID returned from VirusTotal"}

    logger.info(f"Uploaded. Analysis ID: {analysis_id}. Waiting for results...")

    # Step 3: Poll for results
    poll = poll_analysis(analysis_id, max_wait=120)
    if not poll.get("success"):
        return {"success": False, "error": poll.get("error", "Polling failed")}

    return {
        "success": True,
        "data": parse_vt_report(poll["report"]),
        "source": "fresh_scan"
    }
