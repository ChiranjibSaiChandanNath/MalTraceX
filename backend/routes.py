import os
import logging
from flask import Blueprint, request, jsonify, render_template, send_file, current_app
from werkzeug.utils import secure_filename
from static_analysis.hash_checker import get_hashes
from backend.services.analysis_service import analyze_file_sync
import time

main_bp = Blueprint('main', __name__)
logger = logging.getLogger(__name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/analyze', methods=['POST'])
def analyze():
    """Synchronous file analysis."""
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400

    file = request.files['file']
    filename = secure_filename(file.filename)
    if not filename:
        return jsonify({'error': 'No file selected / invalid name'}), 400

    # Save temp
    upload_dir = current_app.config.get('UPLOAD_DIR', 'uploads')
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
        
    temp_path = os.path.join(upload_dir, f"temp_{filename}")
    file.save(temp_path)

    try:
        # Give illusion of deep scan
        time.sleep(1.5)
        
        # Extract Hash
        hashes = get_hashes(temp_path)
        
        # Analyze Synchronously
        app = current_app._get_current_object()
        results = analyze_file_sync(app, temp_path, filename, hashes)
        
        # Clean up temp
        if os.path.exists(temp_path):
             os.remove(temp_path)
        
        return jsonify({
            'status': 'complete',
            'data': results
        })

    except Exception as e:
        logger.exception(f"Critical failure: {e}")
        if os.path.exists(temp_path):
            os.remove(temp_path)
        return jsonify({'error': f'Analysis failed: {str(e)}'}), 500

@main_bp.route('/download_report/<filename>')
def download_report(filename):
    sec_filename = secure_filename(filename)
    if not sec_filename:
        return jsonify({'error': 'Invalid filename'}), 400
        
    report_path = os.path.join(current_app.config.get('REPORT_DIR', 'reports'), sec_filename)
    
    if os.path.exists(report_path):
        return send_file(report_path, as_attachment=True)
    return jsonify({'error': 'Report not found'}), 404
