import hashlib
import logging
from typing import Dict

logger = logging.getLogger(__name__)

def get_hashes(file_path: str) -> Dict[str, str]:
    """Generates MD5, SHA1, and SHA256 hashes for a given file."""
    hashes = {}
    try:
        with open(file_path, 'rb') as f:
            data = f.read()
            hashes['md5']    = hashlib.md5(data).hexdigest()
            hashes['sha1']   = hashlib.sha1(data).hexdigest()
            hashes['sha256'] = hashlib.sha256(data).hexdigest()
    except Exception as e:
        logger.error(f"Failed to hash {file_path}: {e}")
        hashes = {'md5': 'Error', 'sha1': 'Error', 'sha256': 'Error'}
    return hashes