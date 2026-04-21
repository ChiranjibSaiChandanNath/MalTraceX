import os
import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import (
    SimpleDocTemplate, Table, TableStyle, Paragraph,
    Spacer, HRFlowable, Image, KeepTogether
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib import colors

# ── Brand Colors ─────────────────────────────────────────────────────────────
C_BG_DARK    = colors.HexColor('#0f172a')
C_BG_PANEL   = colors.HexColor('#1e293b')
C_BG_ROW_A   = colors.HexColor('#f8fafc')
C_BG_ROW_B   = colors.HexColor('#eef2f7')
C_BORDER     = colors.HexColor('#cbd5e1')
C_ACCENT     = colors.HexColor('#3b82f6')
C_ACCENT2    = colors.HexColor('#06b6d4')
C_WHITE      = colors.HexColor('#ffffff')
C_TEXT_DARK  = colors.HexColor('#1e293b')
C_TEXT_MUTED = colors.HexColor('#64748b')
C_CRITICAL   = colors.HexColor('#dc2626')
C_HIGH       = colors.HexColor('#ea580c')
C_MEDIUM     = colors.HexColor('#ca8a04')
C_LOW        = colors.HexColor('#16a34a')

PAGE_W = 7.5 * inch

_THIS_DIR = os.path.dirname(os.path.abspath(__file__))
LOGO_PATH = os.path.join(os.path.dirname(_THIS_DIR), "frontend", "static", "img", "malware copy.png")


def _risk_color(label):
    return {'Critical': C_CRITICAL, 'High': C_HIGH, 'Medium': C_MEDIUM, 'Low': C_LOW}.get(label, C_TEXT_MUTED)

def _risk_bg(label):
    return {
        'Critical': colors.HexColor('#fef2f2'),
        'High':     colors.HexColor('#fff7ed'),
        'Medium':   colors.HexColor('#fefce8'),
        'Low':      colors.HexColor('#f0fdf4'),
    }.get(label, colors.HexColor('#f8fafc'))

def _section_header(title, accent=C_BG_PANEL):
    t = Table([[title]], colWidths=[PAGE_W])
    t.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), accent),
        ('TEXTCOLOR',     (0,0), (-1,-1), C_WHITE),
        ('FONTNAME',      (0,0), (-1,-1), 'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1), 11),
        ('TOPPADDING',    (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING',   (0,0), (-1,-1), 14),
    ]))
    return t

def _kv_table(rows, col_w=(1.8*inch, 5.7*inch)):
    t = Table(rows, colWidths=list(col_w))
    t.setStyle(TableStyle([
        ('FONTNAME',      (0,0), (0,-1), 'Helvetica-Bold'),
        ('FONTNAME',      (1,0), (1,-1), 'Helvetica'),
        ('FONTSIZE',      (0,0), (-1,-1), 10),
        ('TEXTCOLOR',     (0,0), (-1,-1), C_TEXT_DARK),
        ('BACKGROUND',    (0,0), (0,-1), colors.HexColor('#e2e8f0')),
        ('ROWBACKGROUNDS',(1,0), (1,-1), [C_BG_ROW_A, C_BG_ROW_B]),
        ('GRID',          (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING',    (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING',   (0,0), (-1,-1), 12),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
    ]))
    return t


def generate_report(filename: str, results: dict, output_path: str) -> str:
    doc = SimpleDocTemplate(
        output_path, pagesize=letter,
        rightMargin=0.5*inch, leftMargin=0.5*inch,
        topMargin=0.45*inch, bottomMargin=0.45*inch,
    )
    styles = getSampleStyleSheet()

    st_body = ParagraphStyle('Body', parent=styles['Normal'], fontSize=10, leading=15, textColor=C_TEXT_DARK)
    st_muted = ParagraphStyle('Muted', parent=styles['Normal'], fontSize=9, leading=13, textColor=C_TEXT_MUTED)
    st_mono  = ParagraphStyle('Mono',  parent=styles['Normal'], fontSize=8, leading=12, fontName='Courier', textColor=C_TEXT_DARK, wordWrap='CJK')

    risk          = results.get('risk', {})
    risk_label    = risk.get('label', 'N/A')
    risk_score    = risk.get('score', 0)
    static_score  = risk.get('static_score')
    dynamic_score = risk.get('dynamic_score')
    hashes        = results.get('hashes', {})
    malware_info  = results.get('malware_info', {})
    impact_data   = results.get('impact_data', [])
    suggestions   = results.get('suggestions', [])
    behavior_logs = results.get('behavior_logs', [])
    reasons       = risk.get('reasons', [])
    file_ext      = results.get('file_extension', 'N/A')
    file_size     = results.get('file_size_bytes', 0)
    dynamic_det   = results.get('dynamic_details') or {}
    analysis_src  = results.get('analysis_source', 'Static Analysis')
    now_str       = datetime.datetime.now().strftime('%Y-%m-%d  %H:%M:%S')

    r_color = _risk_color(risk_label)
    r_bg    = _risk_bg(risk_label)
    story   = []

    # ══════════════════════════════════════
    # HEADER BANNER
    # ══════════════════════════════════════
    logo_cell = Paragraph("", styles['Normal'])
    if os.path.exists(LOGO_PATH):
        try:
            logo_cell = Image(LOGO_PATH, width=0.75*inch, height=0.75*inch)
        except Exception:
            pass

    title_para = Paragraph("<b>MalTrace Analyzer</b>",
        ParagraphStyle('HT', parent=styles['Normal'], fontSize=18,
                       fontName='Helvetica-Bold', textColor=C_WHITE, leading=22, alignment=TA_LEFT))
    subtitle_para = Paragraph("Security Analysis Platform  •  Automated Threat Report",
        ParagraphStyle('HS', parent=styles['Normal'], fontSize=10,
                       textColor=C_ACCENT2, leading=14, alignment=TA_LEFT))
    date_para = Paragraph(f"Generated: {now_str}",
        ParagraphStyle('HD', parent=styles['Normal'], fontSize=9,
                       textColor=colors.HexColor('#94a3b8'), alignment=TA_RIGHT, leading=13))

    header_tbl = Table([[logo_cell, [title_para, subtitle_para], date_para]],
                        colWidths=[0.9*inch, 4.5*inch, 2.1*inch])
    header_tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), C_BG_DARK),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING',    (0,0), (-1,-1), 14),
        ('BOTTOMPADDING', (0,0), (-1,-1), 14),
        ('LEFTPADDING',   (0,0), (0,-1),  14),
        ('RIGHTPADDING',  (-1,0),(-1,-1), 14),
    ]))
    story.append(header_tbl)
    story.append(Spacer(1, 0.2*inch))

    # ══════════════════════════════════════
    # SECTION 1 — FILE INFORMATION
    # ══════════════════════════════════════
    story.append(_section_header("📄   FILE INFORMATION"))
    story.append(Spacer(1, 0.06*inch))
    if not file_size:        size_str = "N/A"
    elif file_size < 1024:   size_str = f"{file_size} bytes"
    elif file_size < 1<<20:  size_str = f"{file_size/1024:.1f} KB"
    else:                    size_str = f"{file_size/(1<<20):.2f} MB"

    story.append(_kv_table([
        ["File Name",        filename],
        ["File Type",        file_ext.upper() if file_ext else "N/A"],
        ["File Size",        size_str],
        ["Analysis Engine",  analysis_src],
        ["Analysed",         now_str],
    ]))
    story.append(Spacer(1, 0.2*inch))

    # ══════════════════════════════════════
    # SECTION 2 — THREAT ASSESSMENT
    # ══════════════════════════════════════
    story.append(_section_header("⚠️   THREAT ASSESSMENT", accent=C_BG_DARK))
    story.append(Spacer(1, 0.06*inch))

    _val_style = ParagraphStyle('VB', parent=styles['Normal'], fontSize=26,
                                fontName='Helvetica-Bold', textColor=r_color,
                                alignment=TA_CENTER, leading=30)
    _sub_style = ParagraphStyle('VS', parent=styles['Normal'], fontSize=9,
                                textColor=C_TEXT_MUTED, alignment=TA_CENTER, leading=12)
    _type_style= ParagraphStyle('VT', parent=styles['Normal'], fontSize=11,
                                fontName='Helvetica-Bold', textColor=C_TEXT_DARK,
                                alignment=TA_CENTER, leading=15)

    m_type_clean = malware_info.get('type', 'N/A')
    COL = 2.5*inch

    verdict_tbl = Table([
        [Paragraph(f"<b>{risk_label.upper()}</b>", _val_style),
         Paragraph(f"<b>{risk_score}</b> / 100",    _val_style),
         Paragraph(f"<b>{m_type_clean}</b>",         _type_style)],
        [Paragraph("Overall Verdict",      _sub_style),
         Paragraph("Risk Score",           _sub_style),
         Paragraph("Threat Classification",_sub_style)],
    ], colWidths=[COL, COL, COL], rowHeights=[0.65*inch, 0.30*inch])
    verdict_tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,-1), r_bg),
        ('ALIGN',         (0,0), (-1,-1), 'CENTER'),
        ('VALIGN',        (0,0), (-1,0),  'BOTTOM'),
        ('VALIGN',        (0,1), (-1,1),  'TOP'),
        ('GRID',          (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING',    (0,0), (-1,0),  14),
        ('BOTTOMPADDING', (0,0), (-1,0),  2),
        ('TOPPADDING',    (0,1), (-1,1),  2),
        ('BOTTOMPADDING', (0,1), (-1,1),  10),
        ('LINEAFTER',     (0,0), (1,-1),  0.8, C_BORDER),
    ]))
    story.append(verdict_tbl)
    story.append(Spacer(1, 0.06*inch))

    # Score breakdown row
    score_parts = [f"Final Score: {risk_score}/100"]
    if static_score is not None:
        score_parts.append(f"Static: {static_score}/100")
    if dynamic_score is not None:
        score_parts.append(f"MalTrace Engine: {dynamic_score}/100")

    story.append(Paragraph(
        f"<b>Description:</b>  {malware_info.get('desc', '')}",
        ParagraphStyle('DP', parent=styles['Normal'], fontSize=10, leading=15,
                       textColor=C_TEXT_DARK, leftIndent=10, spaceBefore=4,
                       spaceAfter=4, backColor=r_bg, borderPad=8)))
    story.append(Paragraph(
        f"<i>Score breakdown — {' | '.join(score_parts)}</i>",
        ParagraphStyle('SB', parent=styles['Normal'], fontSize=9, leading=13,
                       textColor=C_TEXT_MUTED, leftIndent=10, spaceAfter=4)))
    story.append(Spacer(1, 0.2*inch))

    # ══════════════════════════════════════
    # SECTION 3 — MALTRACE ENGINE RESULTS
    # ══════════════════════════════════════
    total_eng   = dynamic_det.get('total_engines', 0)
    malicious_e = dynamic_det.get('malicious_engines', 0)
    suspicious_e= dynamic_det.get('suspicious_engines', 0)
    signatures  = dynamic_det.get('signatures', [])
    net_activity= dynamic_det.get('network_activity', [])

    if dynamic_det:
        story.append(_section_header("🔬   MALTRACE ENGINE SCAN RESULTS", accent=colors.HexColor('#0f4c81')))
        story.append(Spacer(1, 0.06*inch))

        clean_e = max(0, total_eng - malicious_e - suspicious_e)
        engine_rows = [
            ["Total Engines Scanned", str(total_eng) if total_eng else "N/A"],
            ["Malicious Detections",  str(malicious_e)],
            ["Suspicious Detections", str(suspicious_e)],
            ["Clean / No Threat",     str(clean_e)],
        ]
        if malware_info.get('family') and malware_info['family'] not in ['Unknown', '']:
            engine_rows.append(["Threat Family", malware_info['family']])

        story.append(_kv_table(engine_rows))
        story.append(Spacer(1, 0.1*inch))

        # Engine detections table
        if signatures:
            story.append(Paragraph("<b>Engine Detections:</b>",
                ParagraphStyle('ED', parent=styles['Normal'], fontSize=10,
                               fontName='Helvetica-Bold', textColor=C_TEXT_DARK, spaceAfter=4)))
            sig_rows = [[Paragraph(f"🛡️  {s}", ParagraphStyle('SR', parent=styles['Normal'],
                          fontSize=9, leading=13, textColor=C_TEXT_DARK))] for s in signatures[:10]]
            sig_tbl = Table(sig_rows, colWidths=[PAGE_W])
            sig_tbl.setStyle(TableStyle([
                ('ROWBACKGROUNDS', (0,0), (-1,-1), [C_BG_ROW_A, C_BG_ROW_B]),
                ('GRID',          (0,0), (-1,-1), 0.5, C_BORDER),
                ('TOPPADDING',    (0,0), (-1,-1), 7),
                ('BOTTOMPADDING', (0,0), (-1,-1), 7),
                ('LEFTPADDING',   (0,0), (-1,-1), 14),
            ]))
            story.append(sig_tbl)
            story.append(Spacer(1, 0.08*inch))

        # File tags
        if net_activity:
            tags_text = "  •  ".join(net_activity[:8])
            story.append(Paragraph(f"<b>File Tags:</b>  {tags_text}",
                ParagraphStyle('FT', parent=styles['Normal'], fontSize=9,
                               leading=14, textColor=C_TEXT_MUTED, leftIndent=10)))

        story.append(Spacer(1, 0.2*inch))

    # ══════════════════════════════════════
    # SECTION 4 — ANALYSIS FINDINGS
    # ══════════════════════════════════════
    story.append(_section_header("🔍   ANALYSIS FINDINGS"))
    story.append(Spacer(1, 0.06*inch))

    _num_sty = ParagraphStyle('FN', parent=styles['Normal'], fontSize=10,
                               fontName='Helvetica-Bold', textColor=C_TEXT_MUTED, alignment=TA_CENTER)
    _rsn_sty = ParagraphStyle('FR', parent=styles['Normal'], fontSize=10, leading=14, textColor=C_TEXT_DARK)

    if not reasons:
        findings_rows = [[Paragraph("1", _num_sty),
                          Paragraph("✅", _num_sty),
                          Paragraph("No malicious indicators detected.", _rsn_sty)]]
    else:
        findings_rows = [
            [Paragraph(str(i+1), _num_sty),
             Paragraph("⚠️", _num_sty),
             Paragraph(r, _rsn_sty)]
            for i, r in enumerate(reasons)
        ]

    findings_tbl = Table(findings_rows, colWidths=[0.38*inch, 0.40*inch, PAGE_W-0.78*inch])
    findings_tbl.setStyle(TableStyle([
        ('FONTSIZE',      (0,0), (-1,-1), 10),
        ('ROWBACKGROUNDS',(0,0), (-1,-1), [C_BG_ROW_A, C_BG_ROW_B]),
        ('BACKGROUND',    (0,0), (1,-1),  colors.HexColor('#e2e8f0')),
        ('GRID',          (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING',    (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING',   (0,0), (1,-1),  6),
        ('LEFTPADDING',   (2,0), (2,-1),  10),
        ('RIGHTPADDING',  (2,0), (2,-1),  12),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
        ('ALIGN',         (0,0), (1,-1),  'CENTER'),
    ]))
    story.append(findings_tbl)
    story.append(Spacer(1, 0.2*inch))

    # ══════════════════════════════════════
    # SECTION 5 — IMPACT & ACTION PLAN
    # ══════════════════════════════════════
    story.append(_section_header("💥   IMPACT ASSESSMENT  &  ACTION PLAN"))
    story.append(Spacer(1, 0.06*inch))

    imp_tbl = Table(
        [["Area", "Level", "Description"]] + [[i['area'], i['level'], i['desc']] for i in impact_data],
        colWidths=[2.0*inch, 1.1*inch, 4.4*inch])
    imp_tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  C_BG_PANEL),
        ('TEXTCOLOR',     (0,0), (-1,0),  C_WHITE),
        ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1), 10),
        ('TEXTCOLOR',     (0,1), (-1,-1), C_TEXT_DARK),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [C_BG_ROW_A, C_BG_ROW_B]),
        ('GRID',          (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING',    (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING',   (0,0), (-1,-1), 10),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(imp_tbl)
    story.append(Spacer(1, 0.1*inch))

    act_tbl = Table(
        [["#", "Recommended Action", "Priority"]] + [[str(s['id']), s['text'], s['priority']] for s in suggestions],
        colWidths=[0.4*inch, 5.5*inch, 1.6*inch])
    act_tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (-1,0),  C_ACCENT),
        ('TEXTCOLOR',     (0,0), (-1,0),  C_WHITE),
        ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (-1,-1), 10),
        ('TEXTCOLOR',     (0,1), (-1,-1), C_TEXT_DARK),
        ('ROWBACKGROUNDS',(0,1), (-1,-1), [C_BG_ROW_A, C_BG_ROW_B]),
        ('GRID',          (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING',    (0,0), (-1,-1), 8),
        ('BOTTOMPADDING', (0,0), (-1,-1), 8),
        ('LEFTPADDING',   (0,0), (-1,-1), 10),
        ('ALIGN',         (0,0), (0,-1),  'CENTER'),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(act_tbl)
    story.append(Spacer(1, 0.2*inch))

    # ══════════════════════════════════════
    # SECTION 6 — BEHAVIOR LOGS
    # ══════════════════════════════════════
    if behavior_logs:
        story.append(_section_header("🖥️   BEHAVIOR LOGS"))
        story.append(Spacer(1, 0.06*inch))

        def _sev_color(s):
            return {'Critical': C_CRITICAL, 'High': C_HIGH, 'Medium': C_MEDIUM, 'Low': C_LOW}.get(s, C_TEXT_MUTED)

        log_rows = []
        for log in behavior_logs:
            sev = log.get('severity', '')
            sev_para = Paragraph(f"<b>{sev}</b>",
                ParagraphStyle('SP', parent=styles['Normal'], fontSize=9,
                               fontName='Helvetica-Bold', textColor=_sev_color(sev), alignment=TA_CENTER))
            log_rows.append([log.get('action',''), log.get('desc',''), sev_para])

        log_tbl = Table([["Action", "Observed Behaviour", "Severity"]] + log_rows,
                        colWidths=[1.5*inch, 4.5*inch, 1.5*inch])
        log_tbl.setStyle(TableStyle([
            ('BACKGROUND',    (0,0), (-1,0),  C_BG_PANEL),
            ('TEXTCOLOR',     (0,0), (-1,0),  C_WHITE),
            ('FONTNAME',      (0,0), (-1,0),  'Helvetica-Bold'),
            ('FONTSIZE',      (0,0), (-1,-1), 10),
            ('TEXTCOLOR',     (0,1), (-1,-1), C_TEXT_DARK),
            ('ROWBACKGROUNDS',(0,1), (-1,-1), [C_BG_ROW_A, C_BG_ROW_B]),
            ('GRID',          (0,0), (-1,-1), 0.5, C_BORDER),
            ('TOPPADDING',    (0,0), (-1,-1), 8),
            ('BOTTOMPADDING', (0,0), (-1,-1), 8),
            ('LEFTPADDING',   (0,0), (-1,-1), 10),
            ('ALIGN',         (2,0), (2,-1),  'CENTER'),
            ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
        ]))
        story.append(log_tbl)
        story.append(Spacer(1, 0.2*inch))

    # ══════════════════════════════════════
    # SECTION 7 — FILE HASHES
    # ══════════════════════════════════════
    story.append(_section_header("🔑   FILE HASHES  (Cryptographic Fingerprints)"))
    story.append(Spacer(1, 0.06*inch))

    hash_tbl = Table([
        ["MD5",    Paragraph(hashes.get('md5',   'N/A'), st_mono)],
        ["SHA-1",  Paragraph(hashes.get('sha1',  'N/A'), st_mono)],
        ["SHA-256",Paragraph(hashes.get('sha256','N/A'), st_mono)],
    ], colWidths=[0.95*inch, PAGE_W-0.95*inch])
    hash_tbl.setStyle(TableStyle([
        ('BACKGROUND',    (0,0), (0,-1),  colors.HexColor('#e2e8f0')),
        ('FONTNAME',      (0,0), (0,-1),  'Helvetica-Bold'),
        ('FONTSIZE',      (0,0), (0,-1),  10),
        ('TEXTCOLOR',     (0,0), (-1,-1), C_TEXT_DARK),
        ('ROWBACKGROUNDS',(1,0), (1,-1),  [C_BG_ROW_A, C_BG_ROW_B]),
        ('GRID',          (0,0), (-1,-1), 0.5, C_BORDER),
        ('TOPPADDING',    (0,0), (-1,-1), 9),
        ('BOTTOMPADDING', (0,0), (-1,-1), 9),
        ('LEFTPADDING',   (0,0), (-1,-1), 12),
        ('VALIGN',        (0,0), (-1,-1), 'MIDDLE'),
    ]))
    story.append(hash_tbl)
    story.append(Spacer(1, 0.25*inch))

    # ══════════════════════════════════════
    # FOOTER
    # ══════════════════════════════════════
    story.append(HRFlowable(width=PAGE_W, thickness=0.5, color=C_BORDER))
    story.append(Spacer(1, 0.08*inch))
    footer_tbl = Table([[
        Paragraph("<b>MalTrace Analyzer</b>  |  Security Analysis Platform",
            ParagraphStyle('FL', parent=styles['Normal'], fontSize=8, textColor=C_TEXT_MUTED, alignment=TA_LEFT)),
        Paragraph(f"Report generated  {now_str}  |  For educational use only",
            ParagraphStyle('FR', parent=styles['Normal'], fontSize=8, textColor=C_TEXT_MUTED, alignment=TA_RIGHT)),
    ]], colWidths=[PAGE_W/2, PAGE_W/2])
    footer_tbl.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'MIDDLE'),('TOPPADDING',(0,0),(-1,-1),0),('BOTTOMPADDING',(0,0),(-1,-1),0)]))
    story.append(footer_tbl)

    doc.build(story)
    return output_path
