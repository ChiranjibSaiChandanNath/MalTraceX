# MalTrace Analyzer — College Major Project
## Dynamic Analysis powered by VirusTotal API (43+ Antivirus Engines)

---

## Project Structure

```
MalTrace-Clean/
├── run.py                          ← Start the app
├── config.py                       ← App configuration
├── requirements.txt                ← Python dependencies
├── backend/
│   ├── app.py                      ← Flask app factory
│   ├── routes.py                   ← API endpoints
│   ├── report_generator.py         ← Auto PDF generator
│   └── services/
│       ├── analysis_service.py     ← Merges static + dynamic results
│       └── hybrid_analysis.py      ← VirusTotal API integration
├── static_analysis/
│   └── hash_checker.py             ← MD5 / SHA1 / SHA256 hashing
├── frontend/
│   ├── index.html                  ← Main UI
│   └── static/
│       ├── css/style.css           ← Styling
│       ├── js/app.js               ← Frontend logic
│       └── img/                    ← Logo images
├── uploads/                        ← Temporary file storage during scan
└── reports/                        ← Generated PDF reports saved here
```

---

## Setup

### 1. Install dependencies
```
pip install -r requirements.txt
```

### 2. Run the project
```
python run.py
```

### 3. Open browser
```
http://localhost:5000
```

---

## API Key Location

File: `backend/services/hybrid_analysis.py`

Line: `VT_API_KEY = "your_virustotal_api_key_here"`

Get your free API key at → https://www.virustotal.com (Sign up → Profile → API Key)

---

## How It Works

```
1. User uploads file via browser
2. hash_checker.py computes MD5, SHA1, SHA256
3. SHA256 hash checked in VirusTotal database (instant if known)
4. If new file → uploaded to VirusTotal for fresh scan
5. 43+ antivirus engines scan the file simultaneously
6. Results returned: threat score, engine detections, file tags
7. Static analysis runs locally: entropy, keywords, PE headers
8. Final Score = (Static × 40%) + (VirusTotal × 60%)
9. Results displayed in UI with full breakdown
10. PDF report auto-generated and saved to /reports/
```

---

## Scoring System

| Score | Label | Verdict |
|---|---|---|
| 85 – 100 | 🔴 CRITICAL | Malicious |
| 60 – 84 | 🟠 HIGH | Malicious |
| 35 – 59 | 🟡 MEDIUM | Suspicious |
| 0 – 34 | 🟢 LOW | Safe |

---

## Analysis Time

VirusTotal hash lookup is **instant** if the file was scanned before.

Fresh file uploads take **20–60 seconds** for results to come back.

The loading screen shows the current step in real time.

---

## PDF Report Sections

Every scan auto-generates a downloadable PDF containing:

1. 📄 File Information
2. ⚠️ Threat Assessment (score + verdict)
3. 🔬 MalTrace Engine Results (engine count + detections)
4. 🔍 Analysis Findings (all security indicators)
5. 💥 Impact Assessment & Action Plan
6. 🖥️ Behavior Logs
7. 🔑 Cryptographic Hashes (MD5, SHA1, SHA256)

---

## Major Project 2026 — Computer Science & Engineering
