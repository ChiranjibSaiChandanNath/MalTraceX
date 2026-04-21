import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    UPLOAD_DIR = os.path.join(BASE_DIR, 'uploads')
    REPORT_DIR = os.path.join(BASE_DIR, 'reports')
    
    # Maximum file upload size: 50MB
    MAX_CONTENT_LENGTH = 50 * 1024 * 1024
    
    # Ensure directories exist
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    os.makedirs(REPORT_DIR, exist_ok=True)
    
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default-dev-secret-key')
    
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{os.path.join(BASE_DIR, 'malware_sandbox.db')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Static Analysis Configurations
    DANGEROUS_APIS = [
        'CreateRemoteThread', 'VirtualAlloc', 'WriteProcessMemory',
        'OpenProcess', 'SetWindowsHookEx', 'RegSetValueEx',
        'ShellExecute', 'WinExec', 'URLDownloadToFile', 'HttpSendRequest', 
        'CryptAcquireContext', 'CreateProcess'
    ]
