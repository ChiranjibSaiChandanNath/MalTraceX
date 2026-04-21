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

## 🏗️ Architecture

<div align="center">

<!-- Architecture diagram: Frontend → Backend → VirusTotal API (SMIL, GitHub-safe) -->
<svg xmlns="http://www.w3.org/2000/svg" width="720" height="380" viewBox="0 0 720 380">
  <defs>
    <marker id="a1" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
      <path d="M0,0 L0,7 L7,3.5 Z" fill="#00ffe7" opacity="0.8"/>
    </marker>
    <marker id="a2" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
      <path d="M0,0 L0,7 L7,3.5 Z" fill="#0080ff" opacity="0.8"/>
    </marker>
    <marker id="a3" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
      <path d="M0,0 L0,7 L7,3.5 Z" fill="#f5a623" opacity="0.8"/>
    </marker>
    <marker id="a4" markerWidth="7" markerHeight="7" refX="6" refY="3.5" orient="auto">
      <path d="M0,0 L0,7 L7,3.5 Z" fill="#00ff88" opacity="0.8"/>
    </marker>
    <linearGradient id="bg1" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00ffe7" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#00ffe7" stop-opacity="0.02"/>
    </linearGradient>
    <linearGradient id="bg2" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#0080ff" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#0080ff" stop-opacity="0.02"/>
    </linearGradient>
    <linearGradient id="bg3" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#f5a623" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#f5a623" stop-opacity="0.02"/>
    </linearGradient>
    <linearGradient id="bg4" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#00ff88" stop-opacity="0.08"/>
      <stop offset="100%" stop-color="#00ff88" stop-opacity="0.02"/>
    </linearGradient>
  </defs>

  <!-- ── LAYER 0: USER ── -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="0.1s" fill="freeze"/>

    <rect x="290" y="8" width="140" height="52" rx="6"
      fill="url(#bg1)" stroke="#00ffe7" stroke-width="1"/>
    <text x="360" y="29" font-family="monospace" font-size="10" fill="#00ffe7"
      text-anchor="middle" letter-spacing="2">USER</text>
    <text x="360" y="45" font-family="monospace" font-size="8" fill="#00ffe7"
      text-anchor="middle" opacity="0.6">Browser · Upload File</text>

    <!-- Corner ticks -->
    <path d="M292,10 L290,10 L290,14" fill="none" stroke="#00ffe7" stroke-width="0.8" opacity="0.5"/>
    <path d="M428,10 L430,10 L430,14" fill="none" stroke="#00ffe7" stroke-width="0.8" opacity="0.5"/>
    <path d="M292,58 L290,58 L290,54" fill="none" stroke="#00ffe7" stroke-width="0.8" opacity="0.5"/>
    <path d="M428,58 L430,58 L430,54" fill="none" stroke="#00ffe7" stroke-width="0.8" opacity="0.5"/>
  </g>

  <!-- Arrow: User → Frontend -->
  <line x1="360" y1="60" x2="360" y2="86" stroke="#00ffe7" stroke-width="1"
    stroke-opacity="0.6" marker-end="url(#a1)" stroke-dasharray="4 3" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="0.5s" fill="freeze"/>
    <animate attributeName="stroke-dashoffset" values="14;0" dur="1s" begin="0.5s" repeatCount="indefinite"/>
  </line>
  <text x="368" y="77" font-family="monospace" font-size="7" fill="#00ffe7" opacity="0">
    HTTP POST
    <animate attributeName="opacity" values="0;0.6" dur="0.3s" begin="0.5s" fill="freeze"/>
  </text>

  <!-- ── LAYER 1: FRONTEND ── -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="0.6s" fill="freeze"/>

    <rect x="210" y="88" width="300" height="64" rx="6"
      fill="url(#bg1)" stroke="#00ffe7" stroke-width="1"/>
    <text x="360" y="110" font-family="monospace" font-size="10" fill="#00ffe7"
      text-anchor="middle" letter-spacing="2">FRONTEND</text>
    <text x="280" y="130" font-family="monospace" font-size="8" fill="#00ffe7"
      text-anchor="middle" opacity="0.55">index.html</text>
    <line x1="320" y1="122" x2="320" y2="146" stroke="#00ffe7" stroke-width="0.4" stroke-opacity="0.2"/>
    <text x="360" y="130" font-family="monospace" font-size="8" fill="#00ffe7"
      text-anchor="middle" opacity="0.55">app.js</text>
    <line x1="400" y1="122" x2="400" y2="146" stroke="#00ffe7" stroke-width="0.4" stroke-opacity="0.2"/>
    <text x="440" y="130" font-family="monospace" font-size="8" fill="#00ffe7"
      text-anchor="middle" opacity="0.55">style.css</text>

    <!-- Pulse dot -->
    <circle cx="494" cy="100" r="3" fill="#00ffe7" opacity="0.4">
      <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="r" values="3;5;3" dur="2s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Arrow: Frontend → Backend -->
  <line x1="360" y1="152" x2="360" y2="178" stroke="#0080ff" stroke-width="1"
    stroke-opacity="0.7" marker-end="url(#a2)" stroke-dasharray="4 3" opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.0s" fill="freeze"/>
    <animate attributeName="stroke-dashoffset" values="14;0" dur="0.8s" begin="1.0s" repeatCount="indefinite"/>
  </line>
  <text x="368" y="169" font-family="monospace" font-size="7" fill="#0080ff" opacity="0">
    REST API
    <animate attributeName="opacity" values="0;0.6" dur="0.3s" begin="1.0s" fill="freeze"/>
  </text>

  <!-- ── LAYER 2: BACKEND ── -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="1.1s" fill="freeze"/>

    <rect x="160" y="180" width="400" height="80" rx="6"
      fill="url(#bg2)" stroke="#0080ff" stroke-width="1"/>
    <text x="360" y="202" font-family="monospace" font-size="10" fill="#0080ff"
      text-anchor="middle" letter-spacing="2">BACKEND  ·  Flask</text>

    <!-- Sub-modules -->
    <rect x="175" y="212" width="82" height="34" rx="3"
      fill="rgba(0,128,255,0.07)" stroke="#0080ff" stroke-width="0.6" stroke-opacity="0.5"/>
    <text x="216" y="227" font-family="monospace" font-size="7.5" fill="#0080ff"
      text-anchor="middle">routes.py</text>
    <text x="216" y="239" font-family="monospace" font-size="6.5" fill="#0080ff"
      text-anchor="middle" opacity="0.5">API endpoints</text>

    <rect x="270" y="212" width="90" height="34" rx="3"
      fill="rgba(0,128,255,0.07)" stroke="#0080ff" stroke-width="0.6" stroke-opacity="0.5"/>
    <text x="315" y="227" font-family="monospace" font-size="7.5" fill="#0080ff"
      text-anchor="middle">app.py</text>
    <text x="315" y="239" font-family="monospace" font-size="6.5" fill="#0080ff"
      text-anchor="middle" opacity="0.5">Flask factory</text>

    <rect x="373" y="212" width="90" height="34" rx="3"
      fill="rgba(0,128,255,0.07)" stroke="#0080ff" stroke-width="0.6" stroke-opacity="0.5"/>
    <text x="418" y="227" font-family="monospace" font-size="7.5" fill="#0080ff"
      text-anchor="middle">hash_check</text>
    <text x="418" y="239" font-family="monospace" font-size="6.5" fill="#0080ff"
      text-anchor="middle" opacity="0.5">MD5/SHA256</text>

    <rect x="474" y="212" width="76" height="34" rx="3"
      fill="rgba(0,128,255,0.07)" stroke="#0080ff" stroke-width="0.6" stroke-opacity="0.5"/>
    <text x="512" y="227" font-family="monospace" font-size="7.5" fill="#0080ff"
      text-anchor="middle">report.py</text>
    <text x="512" y="239" font-family="monospace" font-size="6.5" fill="#0080ff"
      text-anchor="middle" opacity="0.5">PDF gen</text>
  </g>

  <!-- Arrows: Backend → VT API + Static Analysis (fork) -->
  <!-- Left fork to Static Analysis -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.6s" fill="freeze"/>
    <line x1="230" y1="260" x2="160" y2="292" stroke="#f5a623" stroke-width="1"
      stroke-opacity="0.6" marker-end="url(#a3)" stroke-dasharray="4 3">
      <animate attributeName="stroke-dashoffset" values="14;0" dur="0.9s" begin="1.6s" repeatCount="indefinite"/>
    </line>
    <text x="172" y="282" font-family="monospace" font-size="7" fill="#f5a623" opacity="0.7">static</text>
  </g>

  <!-- Right fork to VirusTotal -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="1.6s" fill="freeze"/>
    <line x1="490" y1="260" x2="560" y2="292" stroke="#0080ff" stroke-width="1"
      stroke-opacity="0.6" marker-end="url(#a2)" stroke-dasharray="4 3">
      <animate attributeName="stroke-dashoffset" values="14;0" dur="0.9s" begin="1.6s" repeatCount="indefinite"/>
    </line>
    <text x="516" y="282" font-family="monospace" font-size="7" fill="#0080ff" opacity="0.7">API call</text>
  </g>

  <!-- ── LAYER 3L: STATIC ANALYSIS ── -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="1.9s" fill="freeze"/>

    <rect x="38" y="294" width="200" height="60" rx="6"
      fill="url(#bg3)" stroke="#f5a623" stroke-width="1"/>
    <text x="138" y="316" font-family="monospace" font-size="9" fill="#f5a623"
      text-anchor="middle" letter-spacing="1.5">STATIC ANALYSIS</text>
    <text x="96" y="334" font-family="monospace" font-size="7.5" fill="#f5a623"
      text-anchor="middle" opacity="0.6">Entropy</text>
    <line x1="118" y1="326" x2="118" y2="348" stroke="#f5a623" stroke-width="0.4" stroke-opacity="0.2"/>
    <text x="138" y="334" font-family="monospace" font-size="7.5" fill="#f5a623"
      text-anchor="middle" opacity="0.6">PE Headers</text>
    <line x1="162" y1="326" x2="162" y2="348" stroke="#f5a623" stroke-width="0.4" stroke-opacity="0.2"/>
    <text x="182" y="334" font-family="monospace" font-size="7.5" fill="#f5a623"
      text-anchor="middle" opacity="0.6">Keywords</text>
    <text x="138" y="348" font-family="monospace" font-size="7" fill="#f5a623"
      text-anchor="middle" opacity="0.4">weight: 40%</text>
  </g>

  <!-- ── LAYER 3R: VIRUSTOTAL API ── -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="1.9s" fill="freeze"/>

    <rect x="480" y="294" width="202" height="60" rx="6"
      fill="url(#bg2)" stroke="#0080ff" stroke-width="1"/>
    <text x="581" y="316" font-family="monospace" font-size="9" fill="#0080ff"
      text-anchor="middle" letter-spacing="1.5">VIRUSTOTAL API</text>
    <text x="530" y="334" font-family="monospace" font-size="7.5" fill="#0080ff"
      text-anchor="middle" opacity="0.6">Hash lookup</text>
    <line x1="560" y1="326" x2="560" y2="348" stroke="#0080ff" stroke-width="0.4" stroke-opacity="0.2"/>
    <text x="581" y="334" font-family="monospace" font-size="7.5" fill="#0080ff"
      text-anchor="middle" opacity="0.6">43+ engines</text>
    <line x1="608" y1="326" x2="608" y2="348" stroke="#0080ff" stroke-width="0.4" stroke-opacity="0.2"/>
    <text x="632" y="334" font-family="monospace" font-size="7.5" fill="#0080ff"
      text-anchor="middle" opacity="0.6">Detections</text>
    <text x="581" y="348" font-family="monospace" font-size="7" fill="#0080ff"
      text-anchor="middle" opacity="0.4">weight: 60%</text>

    <!-- Spinning ring on VT box -->
    <circle cx="669" cy="302" r="7" fill="none" stroke="#0080ff" stroke-width="0.8"
      stroke-dasharray="5 4" stroke-opacity="0.5">
      <animateTransform attributeName="transform" type="rotate"
        from="0 669 302" to="360 669 302" dur="4s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Arrows: both converge to Final Score -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.3s" begin="2.4s" fill="freeze"/>
    <line x1="138" y1="354" x2="295" y2="370" stroke="#00ff88" stroke-width="1"
      stroke-opacity="0.6" marker-end="url(#a4)" stroke-dasharray="4 3">
      <animate attributeName="stroke-dashoffset" values="14;0" dur="0.9s" begin="2.4s" repeatCount="indefinite"/>
    </line>
    <line x1="581" y1="354" x2="430" y2="370" stroke="#00ff88" stroke-width="1"
      stroke-opacity="0.6" marker-end="url(#a4)" stroke-dasharray="4 3">
      <animate attributeName="stroke-dashoffset" values="14;0" dur="0.9s" begin="2.4s" repeatCount="indefinite"/>
    </line>
  </g>

  <!-- ── LAYER 4: FINAL SCORE ── -->
  <g opacity="0">
    <animate attributeName="opacity" values="0;1" dur="0.4s" begin="2.7s" fill="freeze"/>

    <rect x="258" y="356" width="204" height="18" rx="4"
      fill="url(#bg4)" stroke="#00ff88" stroke-width="1"/>
    <text x="360" y="369" font-family="monospace" font-size="8.5" fill="#00ff88"
      text-anchor="middle" letter-spacing="2">FINAL SCORE  ·  PDF REPORT</text>

    <!-- Blink -->
    <circle cx="452" cy="365" r="3" fill="#00ff88">
      <animate attributeName="opacity" values="1;0.2;1" dur="1.5s" begin="3s" repeatCount="indefinite"/>
    </circle>
  </g>
</svg>

</div>

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
