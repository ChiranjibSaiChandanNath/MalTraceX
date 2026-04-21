let lastReportFilename = '';

document.addEventListener('DOMContentLoaded', () => {
    const fileInput    = document.getElementById('fileInput');
    const fileLabelText = document.getElementById('fileLabelText');
    const uploadCard   = document.getElementById('uploadCard');

    fileInput.addEventListener('change', (e) => {
        if (e.target.files.length > 0) {
            fileLabelText.textContent = e.target.files[0].name;
            uploadCard.style.borderColor = '#1e293b';
        }
    });

    uploadCard.addEventListener('dragover',  (e) => { e.preventDefault(); uploadCard.classList.add('drag-over'); });
    uploadCard.addEventListener('dragleave', (e) => { e.preventDefault(); uploadCard.classList.remove('drag-over'); });
    uploadCard.addEventListener('drop', (e) => {
        e.preventDefault();
        uploadCard.classList.remove('drag-over');
        if (e.dataTransfer.files.length > 0) {
            fileInput.files = e.dataTransfer.files;
            fileLabelText.textContent = fileInput.files[0].name;
            uploadCard.style.borderColor = '#3b82f6';
        }
    });
});

const STEPS = [
    { id: 'step1', text: 'Reading file & computing hashes...' },
    { id: 'step2', text: 'Checking MalTrace threat database...' },
    { id: 'step3', text: 'Scanning with 70+ antivirus engines...' },
    { id: 'step4', text: 'Building your threat report...' },
];

async function animateSteps() {
    const els = STEPS.map(s => document.getElementById(s.id));
    els.forEach((el, i) => { if (el) { el.style.opacity = 0; el.textContent = STEPS[i].text; } });
    for (let i = 0; i < els.length; i++) {
        await new Promise(r => setTimeout(r, 700));
        if (els[i]) { els[i].style.opacity = 1; els[i].textContent = '✅ ' + STEPS[i].text; }
    }
}

async function analyzeFile() {
    const fileInput = document.getElementById('fileInput');
    if (!fileInput.files[0]) { alert('⚠️ Please select a file first!'); return; }

    const btn = document.getElementById('analyzeBtn');
    btn.disabled = true;
    document.getElementById('results').style.display = 'none';
    document.getElementById('loader').style.display  = 'block';

    const animPromise = animateSteps();
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        const response = await fetch('/analyze', { method: 'POST', body: formData });
        const data     = await response.json();
        await animPromise;
        await new Promise(r => setTimeout(r, 400));
        if (!response.ok || data.error) throw new Error(data.error || 'Server error');
        handleAnalysisComplete(data.data, fileInput.files[0].name);
    } catch (err) {
        handleAnalysisError(err);
    }
}

function handleAnalysisComplete(data, filename) {
    document.getElementById('loader').style.display = 'none';
    document.getElementById('analyzeBtn').disabled  = false;
    lastReportFilename = data.report_filename;

    const risk        = data.risk         || {};
    const malwareInfo = data.malware_info || {};
    const impacts     = data.impact_data  || [];
    const suggestions = data.suggestions  || [];
    const dynamic     = data.dynamic_details || null;
    const source      = data.analysis_source || 'Static Analysis';

    // Verdict colours
    let verdictText = 'SAFE', verdictColor = '#22c55e';
    let verdictBg = 'rgba(34,197,94,0.1)', verdictBorder = 'border-green';
    if (risk.label === 'Critical' || risk.label === 'High') {
        verdictText = 'MALICIOUS'; verdictColor = '#ef4444';
        verdictBg = 'rgba(239,68,68,0.1)'; verdictBorder = 'border-red';
    } else if (risk.label === 'Medium') {
        verdictText = 'SUSPICIOUS'; verdictColor = '#facc15';
        verdictBg = 'rgba(250,204,21,0.1)'; verdictBorder = 'border-yellow';
    }

    // Score line — only show MalTrace score, remove static
    const dynamicBadge = risk.dynamic_score != null ? `<span style="font-size:13px;color:#38bdf8;margin-left:12px;">MalTrace: ${risk.dynamic_score}/100</span>` : '';

    const sourceBadge = `<div style="margin-top:10px;">
        <span style="background:rgba(56,189,248,0.15);color:#38bdf8;border:1px solid rgba(56,189,248,0.3);padding:4px 14px;border-radius:20px;font-size:12px;font-weight:600;">
            🔬 MalTrace Engine + Dynamic Analysis
        </span></div>`;

    // Impact rows
    const impactHTML = impacts.map(imp => {
        const c = imp.level.includes('🔴') ? '#ef4444' : imp.level.includes('🟡') ? '#facc15' : '#22c55e';
        return `<tr>
            <td style="padding:12px;font-weight:500;">${imp.area}</td>
            <td style="padding:12px;color:${c};font-weight:bold;">${imp.level}</td>
        </tr>
        <tr><td colspan="2" style="padding:0 12px 12px;color:var(--text-muted);font-size:13px;border-bottom:1px solid var(--border-color);">${imp.desc}</td></tr>`;
    }).join('');

    // Suggestion rows
    const suggestHTML = suggestions.map(s => `
        <tr style="border-bottom:1px solid var(--border-color);">
            <td style="padding:12px;">${s.id}</td>
            <td style="padding:12px;font-weight:500;">${s.text}</td>
            <td style="padding:12px;">${s.priority}</td>
        </tr>`).join('');

    // Reasons - single merged table instead of separate accordions
    const reasonsHTML = `
        <table style="width:100%;border-collapse:collapse;font-size:13px;">
            <thead>
                <tr style="background:rgba(56,189,248,0.1);border-bottom:2px solid var(--border-color);">
                    <th style="padding:10px 12px;text-align:left;color:var(--text-muted);width:40px;">#</th>
                    <th style="padding:10px 12px;text-align:left;color:var(--text-muted);">Security Finding</th>
                </tr>
            </thead>
            <tbody>
                ${(risk.reasons || []).map((r, i) => `
                    <tr style="border-bottom:1px solid var(--border-color);background:${i%2===0?'transparent':'rgba(255,255,255,0.02)'};">
                        <td style="padding:10px 12px;color:var(--text-muted);font-weight:600;">${i+1}</td>
                        <td style="padding:10px 12px;color:var(--text-secondary);">🔍 ${r}</td>
                    </tr>`).join('')}
            </tbody>
        </table>`;

    // VirusTotal dynamic section
    let dynamicSection = '';
    if (dynamic) {
        const malicious  = dynamic.malicious_engines  || 0;
        const suspicious = dynamic.suspicious_engines || 0;
        const total      = dynamic.total_engines      || 0;
        const clean      = total - malicious - suspicious;

        // Engine meter bar
        const meterHTML = total > 0 ? `
            <div style="margin:12px 0;">
                <div style="display:flex;justify-content:space-between;font-size:12px;margin-bottom:4px;">
                    <span style="color:#ef4444;">🔴 Malicious: ${malicious}</span>
                    <span style="color:#facc15;">🟡 Suspicious: ${suspicious}</span>
                    <span style="color:#22c55e;">🟢 Clean: ${clean}</span>
                </div>
                <div style="background:#1a1a2e;border-radius:8px;height:12px;overflow:hidden;display:flex;">
                    <div style="background:#ef4444;width:${(malicious/total)*100}%;"></div>
                    <div style="background:#facc15;width:${(suspicious/total)*100}%;"></div>
                    <div style="background:#22c55e;width:${(clean/total)*100}%;"></div>
                </div>
                <p style="font-size:12px;color:var(--text-muted);margin-top:6px;text-align:right;">${total} total engines scanned</p>
            </div>` : '';

        const sigsHTML = dynamic.signatures.length
            ? dynamic.signatures.slice(0, 8).map(s => `<div style="padding:6px 0;border-bottom:1px solid var(--border-color);font-size:12px;color:var(--text-secondary);">🛡️ ${s}</div>`).join('')
            : '<p style="color:var(--text-muted);font-size:13px;">No detections found</p>';

        const tagsHTML = dynamic.network_activity.length
            ? dynamic.network_activity.map(t => `<span style="display:inline-block;background:rgba(56,189,248,0.1);color:#38bdf8;border:1px solid rgba(56,189,248,0.3);padding:3px 10px;border-radius:10px;font-size:12px;margin:3px;">${t}</span>`).join('')
            : '<span style="color:var(--text-muted);font-size:13px;">No tags found</span>';

        dynamicSection = `
        <div class="card" style="border-top:2px solid #38bdf8;">
            <h3 style="color:#38bdf8;">🔬 MalTrace Scan Results
                <span style="font-size:12px;font-weight:400;color:var(--text-muted);"> — ${malicious + suspicious} detections across ${malicious + suspicious + clean} antivirus engines</span>
            </h3>
            ${meterHTML}
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-top:16px;">
                <div>
                    <p style="font-size:12px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">Engine Detections</p>
                    ${sigsHTML}
                </div>
                <div>
                    <p style="font-size:12px;color:var(--text-muted);text-transform:uppercase;letter-spacing:1px;margin-bottom:8px;">File Tags</p>
                    ${tagsHTML}
                </div>
            </div>
        </div>`;
    }

    const resultsSection = document.getElementById('results');
    resultsSection.innerHTML = `
        <!-- Verdict -->
        <div class="card verdict-card ${verdictBorder}" style="background-color:${verdictBg};text-align:center;padding:40px;margin-bottom:24px;">
            <h2 style="font-size:48px;color:${verdictColor};margin-bottom:8px;">${verdictText}</h2>
            <p style="font-size:18px;font-weight:600;margin-bottom:4px;">${data.filename} • ${(data.file_extension||'FILE').toUpperCase()}</p>
            <p style="font-size:14px;color:var(--text-muted);margin-bottom:8px;">
                Risk Score: <strong style="color:${verdictColor}">${risk.score}/100</strong>${dynamicBadge}
            </p>
            ${sourceBadge}
        </div>

        <div class="vertical-layout">
            <!-- Malware Classification -->
            <div class="card">
                <h3>Malware Classification</h3>
                <div style="display:flex;align-items:center;gap:16px;margin-top:16px;">
                    <div style="font-size:40px;background:rgba(0,0,0,0.2);padding:16px;border-radius:12px;">${malwareInfo.type.split(' ')[0]}</div>
                    <div>
                        <h4 style="font-size:20px;font-weight:600;margin-bottom:4px;">${malwareInfo.type.replace(/^[^\w]+/,'').trim()}</h4>
                        <p style="color:var(--text-secondary);line-height:1.4;">${malwareInfo.desc}</p>
                        ${malwareInfo.family && malwareInfo.family !== 'Unknown'
                            ? `<p style="margin-top:6px;font-size:12px;color:#38bdf8;">Threat Label: ${malwareInfo.family}</p>` : ''}
                    </div>
                </div>
            </div>

            <!-- VirusTotal Results -->
            ${dynamicSection}

            <div class="split-layout">
                <!-- Impact -->
                <div class="card">
                    <h3>Impact Assessment</h3>
                    <table style="width:100%;border-collapse:collapse;margin-top:16px;text-align:left;">
                        <tbody>${impactHTML}</tbody>
                    </table>
                </div>

                <!-- Suggestions -->
                <div class="card">
                    <h3>Action Plan</h3>
                    <table style="width:100%;border-collapse:collapse;margin-top:16px;text-align:left;font-size:14px;">
                        <thead>
                            <tr style="border-bottom:2px solid var(--border-color);color:var(--text-muted);">
                                <th style="padding:12px;width:40px;">#</th>
                                <th style="padding:12px;">Suggestion</th>
                                <th style="padding:12px;">Priority</th>
                            </tr>
                        </thead>
                        <tbody>${suggestHTML}</tbody>
                    </table>
                </div>
            </div>

            <!-- Technical Details -->
            <div class="card">
                <h3>Technical Details (What did we check?)</h3>
                <p style="color:var(--text-muted);margin-top:4px;margin-bottom:16px;">All security indicators that contributed to the final verdict.</p>
                ${reasonsHTML}
            </div>

            <!-- Actions -->
            <div style="display:flex;gap:16px;margin-top:32px;flex-wrap:wrap;">
                <button class="btn btn-primary" style="flex:1;min-width:250px;" onclick="downloadReport()">
                    <i class="ph-bold ph-file-pdf" style="font-size:20px;vertical-align:middle;margin-right:6px;"></i> Download PDF Report
                </button>
                <button class="btn btn-outline" style="flex:1;min-width:250px;" onclick="scanAgain()">🔄 Analyze Another File</button>
            </div>
        </div>`;

    resultsSection.style.display = 'block';
    resultsSection.scrollIntoView({ behavior: 'smooth', block: 'start' });
}

function handleAnalysisError(err) {
    document.getElementById('loader').style.display = 'none';
    document.getElementById('analyzeBtn').disabled  = false;
    const s = document.getElementById('results');
    s.innerHTML = `
        <div class="card border-red" style="text-align:center;padding:40px;">
            <span style="font-size:64px;">❌</span>
            <h2 style="margin:20px 0;color:#ef4444;">Analysis Error</h2>
            <p style="color:var(--text-secondary);">${err.message}</p>
        </div>
        <div style="text-align:center;margin-top:20px;">
            <button class="btn btn-outline" onclick="scanAgain()">Try Again</button>
        </div>`;
    s.style.display = 'block';
}

function scanAgain() {
    document.getElementById('results').innerHTML = '';
    document.getElementById('results').style.display = 'none';
    document.getElementById('fileInput').value = '';
    document.getElementById('fileLabelText').textContent = 'Choose a file...';
    document.getElementById('uploadCard').style.borderColor = 'var(--border-color)';
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

function downloadReport() {
    if (lastReportFilename)
        window.open('/download_report/' + encodeURIComponent(lastReportFilename), '_blank');
}

window.toggleAccordion = function(h) {
    const c = h.nextElementSibling;
    const v = c.style.display === 'block';
    c.style.display = v ? 'none' : 'block';
    h.querySelector('.icon').textContent = v ? '▼' : '▲';
}
