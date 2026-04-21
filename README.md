<div align="center">

<!-- Animated shield SVG (SMIL — GitHub safe) -->
<img src="https://readme-typing-svg.demolab.com?font=Orbitron&weight=900&size=32&duration=3000&pause=1000&color=00FFE7&center=true&vCenter=true&width=600&lines=MalTrace+Analyzer;Dynamic+Malware+Analysis;43%2B+Antivirus+Engines" alt="MalTrace Analyzer" />

<br/>

<!-- Animated radar/scanner SVG -->
<svg xmlns="http://www.w3.org/2000/svg" width="160" height="160" viewBox="0 0 160 160">
  <defs>
    <radialGradient id="rg" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00ffe7" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#000" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <!-- Background circles -->
  <circle cx="80" cy="80" r="70" fill="none" stroke="#00ffe7" stroke-width="0.6" stroke-opacity="0.2"/>
  <circle cx="80" cy="80" r="52" fill="none" stroke="#00ffe7" stroke-width="0.6" stroke-opacity="0.2"/>
  <circle cx="80" cy="80" r="34" fill="none" stroke="#00ffe7" stroke-width="0.6" stroke-opacity="0.2"/>

  <!-- Crosshair lines -->
  <line x1="80" y1="10" x2="80" y2="150" stroke="#00ffe7" stroke-width="0.5" stroke-opacity="0.2"/>
  <line x1="10" y1="80" x2="150" y2="80" stroke="#00ffe7" stroke-width="0.5" stroke-opacity="0.2"/>

  <!-- Outer spinning dashed ring -->
  <circle cx="80" cy="80" r="68" fill="none" stroke="#00ffe7" stroke-width="1.2"
    stroke-dasharray="14 8" stroke-linecap="round" stroke-opacity="0.7">
    <animateTransform attributeName="transform" type="rotate"
      from="0 80 80" to="360 80 80" dur="8s" repeatCount="indefinite"/>
  </circle>

  <!-- Inner counter-rotating ring -->
  <circle cx="80" cy="80" r="56" fill="none" stroke="#0080ff" stroke-width="0.8"
    stroke-dasharray="6 5" stroke-opacity="0.5">
    <animateTransform attributeName="transform" type="rotate"
      from="360 80 80" to="0 80 80" dur="5s" repeatCount="indefinite"/>
  </circle>

  <!-- Radar sweep -->
  <g>
    <animateTransform attributeName="transform" type="rotate"
      from="0 80 80" to="360 80 80" dur="2.5s" repeatCount="indefinite"/>
    <line x1="80" y1="80" x2="80" y2="12" stroke="#00ffe7" stroke-width="1.5" stroke-opacity="0.9"/>
    <ellipse cx="80" cy="80" rx="68" ry="68"
      fill="url(#rg)" stroke="none" clip-path="none" opacity="0.5"/>
  </g>

  <!-- Center shield -->
  <path d="M80,55 L100,65 L100,80 Q100,95 80,104 Q60,95 60,80 L60,65 Z"
    fill="rgba(0,255,231,0.07)" stroke="#00ffe7" stroke-width="1.2">
    <animate attributeName="stroke-opacity" values="0.5;1;0.5" dur="2s" repeatCount="indefinite"/>
  </path>

  <!-- Bug body inside shield -->
  <ellipse cx="80" cy="79" rx="5" ry="7" fill="none" stroke="#00ffe7" stroke-width="1">
    <animate attributeName="stroke-opacity" values="0.6;1;0.6" dur="1.5s" repeatCount="indefinite"/>
  </ellipse>
  <line x1="75" y1="74" x2="70" y2="70" stroke="#00ffe7" stroke-width="0.8" stroke-opacity="0.6"/>
  <line x1="75" y1="79" x2="69" y2="79" stroke="#00ffe7" stroke-width="0.8" stroke-opacity="0.6"/>
  <line x1="75" y1="84" x2="70" y2="88" stroke="#00ffe7" stroke-width="0.8" stroke-opacity="0.6"/>
  <line x1="85" y1="74" x2="90" y2="70" stroke="#00ffe7" stroke-width="0.8" stroke-opacity="0.6"/>
  <line x1="85" y1="79" x2="91" y2="79" stroke="#00ffe7" stroke-width="0.8" stroke-opacity="0.6"/>
  <line x1="85" y1="84" x2="90" y2="88" stroke="#00ffe7" stroke-width="0.8" stroke-opacity="0.6"/>

  <!-- Blinking dots -->
  <circle cx="22" cy="30" r="2" fill="#00ffe7">
    <animate attributeName="opacity" values="0;1;0" dur="2s" begin="0.3s" repeatCount="indefinite"/>
  </circle>
  <circle cx="138" cy="110" r="2" fill="#0080ff">
    <animate attributeName="opacity" values="0;1;0" dur="2.5s" begin="0.9s" repeatCount="indefinite"/>
  </circle>
  <circle cx="130" cy="28" r="1.5" fill="#00ff88">
    <animate attributeName="opacity" values="0;1;0" dur="1.8s" begin="1.4s" repeatCount="indefinite"/>
  </circle>
  <circle cx="25" cy="120" r="1.5" fill="#ff3c6e">
    <animate attributeName="opacity" values="0;1;0" dur="2.2s" begin="0.6s" repeatCount="indefinite"/>
  </circle>
</svg>

<br/>

![Python](https://img.shields.io/badge/Python-3.x-00ffe7?style=for-the-badge&logo=python&logoColor=black&labelColor=060f1e)
![Flask](https://img.shields.io/badge/Flask-Backend-00ffe7?style=for-the-badge&logo=flask&logoColor=black&labelColor=060f1e)
![VirusTotal](https://img.shields.io/badge/VirusTotal-API-ff3c6e?style=for-the-badge&logo=virustotal&logoColor=white&labelColor=060f1e)
![Engines](https://img.shields.io/badge/AV_Engines-43%2B-f5a623?style=for-the-badge&labelColor=060f1e)
![Status](https://img.shields.io/badge/Status-Active-00ff88?style=for-the-badge&labelColor=060f1e)

<br/>

> **Dynamic malware analysis powered by VirusTotal API — College Major Project 2026**

</div>

---

## 📁 Project Structure

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

## ⚙️ Setup

### 1 · Install dependencies
```bash
pip install -r requirements.txt
```

### 2 · Run the project
```bash
python run.py
```

### 3 · Open browser
```
http://localhost:5000
```

---

## 🔑 API Key Location

| File | Line |
|------|------|
| `backend/services/hybrid_analysis.py` | `VT_API_KEY = "your_virustotal_api_key_here"` |

Get your free API key → **[virustotal.com](https://www.virustotal.com)** › Sign up › Profile › API Key

---

## ⚡ How It Works

<!-- Animated pipeline SVG -->
<div align="center">
<svg xmlns="http://www.w3.org/2000/svg" width="700" height="60" viewBox="0 0 700 60">
  <defs>
    <marker id="arr" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L0,6 L6,3 Z" fill="#00ffe7" opacity="0.7"/>
    </marker>
  </defs>

  <!-- Step boxes -->
  <g font-family="monospace" font-size="9" fill="#00ffe7" text-anchor="middle">

    <!-- Upload -->
    <rect x="1" y="15" width="72" height="28" rx="3" fill="rgba(0,255,231,0.07)" stroke="#00ffe7" stroke-width="0.8" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.1s" fill="freeze"/>
    </rect>
    <text x="37" y="32" opacity="0">UPLOAD<animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.1s" fill="freeze"/></text>
    <line x1="73" y1="29" x2="98" y2="29" stroke="#00ffe7" stroke-width="0.8" stroke-opacity="0.5" marker-end="url(#arr)" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.3s" fill="freeze"/>
    </line>

    <!-- Hash -->
    <rect x="99" y="15" width="72" height="28" rx="3" fill="rgba(0,128,255,0.07)" stroke="#0080ff" stroke-width="0.8" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.4s" fill="freeze"/>
    </rect>
    <text x="135" y="32" fill="#0080ff" opacity="0">HASH<animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.4s" fill="freeze"/></text>
    <line x1="171" y1="29" x2="196" y2="29" stroke="#00ffe7" stroke-width="0.8" stroke-opacity="0.5" marker-end="url(#arr)" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.6s" fill="freeze"/>
    </line>

    <!-- VT Lookup -->
    <rect x="197" y="15" width="80" height="28" rx="3" fill="rgba(0,255,231,0.07)" stroke="#00ffe7" stroke-width="0.8" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.7s" fill="freeze"/>
    </rect>
    <text x="237" y="32" opacity="0">VT LOOKUP<animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.7s" fill="freeze"/></text>
    <line x1="277" y1="29" x2="302" y2="29" stroke="#00ffe7" stroke-width="0.8" stroke-opacity="0.5" marker-end="url(#arr)" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.9s" fill="freeze"/>
    </line>

    <!-- 43+ AV -->
    <rect x="303" y="15" width="72" height="28" rx="3" fill="rgba(255,60,110,0.07)" stroke="#ff3c6e" stroke-width="0.8" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.0s" fill="freeze"/>
    </rect>
    <text x="339" y="32" fill="#ff3c6e" opacity="0">43+ SCAN<animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.0s" fill="freeze"/></text>
    <line x1="375" y1="29" x2="400" y2="29" stroke="#00ffe7" stroke-width="0.8" stroke-opacity="0.5" marker-end="url(#arr)" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.2s" fill="freeze"/>
    </line>

    <!-- Static -->
    <rect x="401" y="15" width="80" height="28" rx="3" fill="rgba(245,166,35,0.07)" stroke="#f5a623" stroke-width="0.8" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.3s" fill="freeze"/>
    </rect>
    <text x="441" y="32" fill="#f5a623" opacity="0">STATIC+PE<animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.3s" fill="freeze"/></text>
    <line x1="481" y1="29" x2="506" y2="29" stroke="#00ffe7" stroke-width="0.8" stroke-opacity="0.5" marker-end="url(#arr)" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.5s" fill="freeze"/>
    </line>

    <!-- Score -->
    <rect x="507" y="15" width="72" height="28" rx="3" fill="rgba(0,255,136,0.07)" stroke="#00ff88" stroke-width="0.8" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.6s" fill="freeze"/>
    </rect>
    <text x="543" y="32" fill="#00ff88" opacity="0">SCORE<animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.6s" fill="freeze"/></text>
    <line x1="579" y1="29" x2="604" y2="29" stroke="#00ffe7" stroke-width="0.8" stroke-opacity="0.5" marker-end="url(#arr)" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.8s" fill="freeze"/>
    </line>

    <!-- PDF -->
    <rect x="605" y="15" width="72" height="28" rx="3" fill="rgba(0,255,231,0.07)" stroke="#00ffe7" stroke-width="0.8" opacity="0">
      <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.9s" fill="freeze"/>
    </rect>
    <text x="641" y="27" opacity="0">PDF<animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.9s" fill="freeze"/></text>
    <text x="641" y="38" opacity="0">REPORT<animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.9s" fill="freeze"/></text>
  </g>
</svg>
</div>

<br/>

```
1.  User uploads file via browser
2.  hash_checker.py computes MD5, SHA1, SHA256
3.  SHA256 hash checked in VirusTotal database  (instant if known)
4.  If new file → uploaded to VirusTotal for fresh scan
5.  43+ antivirus engines scan the file simultaneously
6.  Results returned: threat score, engine detections, file tags
7.  Static analysis runs locally: entropy, keywords, PE headers
8.  Final Score = (Static × 40%) + (VirusTotal × 60%)
9.  Results displayed in UI with full breakdown
10. PDF report auto-generated and saved to /reports/
```

---

## 🎯 Scoring System

<!-- Animated score meter SVG -->
<div align="center">
<svg xmlns="http://www.w3.org/2000/svg" width="500" height="36" viewBox="0 0 500 36">
  <defs>
    <linearGradient id="scoreGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%"   stop-color="#00ff88"/>
      <stop offset="35%"  stop-color="#f5a623"/>
      <stop offset="60%"  stop-color="#ff7c2a"/>
      <stop offset="100%" stop-color="#ff3c6e"/>
    </linearGradient>
  </defs>
  <!-- Track -->
  <rect x="10" y="14" width="480" height="8" rx="4" fill="rgba(255,255,255,0.05)" stroke="rgba(255,255,255,0.1)" stroke-width="0.5"/>
  <!-- Animated fill -->
  <rect x="10" y="14" width="0" height="8" rx="4" fill="url(#scoreGrad)">
    <animate attributeName="width" from="0" to="480" dur="2s" begin="0.5s" fill="freeze"/>
  </rect>
  <!-- Labels -->
  <text x="10"  y="9" font-family="monospace" font-size="7" fill="#00ff88">0 · SAFE</text>
  <text x="165" y="9" font-family="monospace" font-size="7" fill="#f5a623" text-anchor="middle">35 · SUSPICIOUS</text>
  <text x="300" y="9" font-family="monospace" font-size="7" fill="#ff7c2a" text-anchor="middle">60 · HIGH</text>
  <text x="480" y="9" font-family="monospace" font-size="7" fill="#ff3c6e" text-anchor="end">85–100 · CRITICAL</text>
  <!-- Tick marks -->
  <line x1="178" y1="12" x2="178" y2="24" stroke="#f5a623" stroke-width="0.8" stroke-opacity="0.6"/>
  <line x1="298" y1="12" x2="298" y2="24" stroke="#ff7c2a" stroke-width="0.8" stroke-opacity="0.6"/>
  <line x1="416" y1="12" x2="416" y2="24" stroke="#ff3c6e" stroke-width="0.8" stroke-opacity="0.6"/>
</svg>
</div>

<br/>

| Score | Indicator | Label | Verdict |
|:-----:|:---------:|-------|---------|
| 85 – 100 | 🔴 | **CRITICAL** | Malicious |
| 60 – 84  | 🟠 | **HIGH**     | Malicious |
| 35 – 59  | 🟡 | **MEDIUM**   | Suspicious |
| 0 – 34   | 🟢 | **LOW**      | Safe |

---

## ⏱️ Analysis Time

| File Type | Method | Time |
|-----------|--------|------|
| **Known file** | VirusTotal hash lookup | ⚡ Instant |
| **New file** | Full upload + scan | 🕐 20–60 seconds |

> The loading screen shows the current step in real time.

---

## 📄 PDF Report Sections

Every scan auto-generates a downloadable PDF containing:

| # | Section |
|---|---------|
| 1 | 📄 File Information |
| 2 | ⚠️ Threat Assessment (score + verdict) |
| 3 | 🔬 MalTrace Engine Results (engine count + detections) |
| 4 | 🔍 Analysis Findings (all security indicators) |
| 5 | 💥 Impact Assessment & Action Plan |
| 6 | 🖥️ Behavior Logs |
| 7 | 🔑 Cryptographic Hashes (MD5, SHA1, SHA256) |

---

<div align="center">

<!-- Animated bottom banner SVG -->
<svg xmlns="http://www.w3.org/2000/svg" width="600" height="48" viewBox="0 0 600 48">
  <defs>
    <linearGradient id="bannerGrad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#00ffe7" stop-opacity="0"/>
      <stop offset="25%" stop-color="#00ffe7" stop-opacity="0.6"/>
      <stop offset="75%" stop-color="#00ffe7" stop-opacity="0.6"/>
      <stop offset="100%" stop-color="#00ffe7" stop-opacity="0"/>
    </linearGradient>
  </defs>
  <!-- Top line -->
  <rect x="0" y="0" width="600" height="1" fill="url(#bannerGrad)"/>
  <!-- Bottom line -->
  <rect x="0" y="47" width="600" height="1" fill="url(#bannerGrad)"/>
  <!-- Text -->
  <text x="300" y="20" font-family="'Courier New', monospace" font-size="11"
    fill="#00ffe7" text-anchor="middle" letter-spacing="4" opacity="0.9">
    MAJOR PROJECT 2026
    <animate attributeName="opacity" values="0.5;1;0.5" dur="3s" repeatCount="indefinite"/>
  </text>
  <text x="300" y="38" font-family="'Courier New', monospace" font-size="9"
    fill="#4a6a8a" text-anchor="middle" letter-spacing="3">
    COMPUTER SCIENCE AND ENGINEERING
  </text>
  <!-- Corner accents -->
  <path d="M8,4 L4,4 L4,14" fill="none" stroke="#00ffe7" stroke-width="1" opacity="0.6"/>
  <path d="M592,4 L596,4 L596,14" fill="none" stroke="#00ffe7" stroke-width="1" opacity="0.6"/>
  <path d="M8,44 L4,44 L4,34" fill="none" stroke="#00ffe7" stroke-width="1" opacity="0.6"/>
  <path d="M592,44 L596,44 L596,34" fill="none" stroke="#00ffe7" stroke-width="1" opacity="0.6"/>
</svg>

<br/><br/>

![Visitors](https://visitor-badge.laobi.icu/badge?page_id=maltrace.analyzer&left_color=060f1e&right_color=00ffe7&left_text=Visitors)

</div>
