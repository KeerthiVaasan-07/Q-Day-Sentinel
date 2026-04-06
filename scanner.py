import re
import os

# Definitions of what we consider "Vulnerable" to Quantum or Classical attacks
RULES = {
    "RSA-2048": r"RSA\.generate\(2048\)",
    "RSA-1024": r"RSA\.generate\(1024\)",
    "AES-CBC": r"AES\.MODE_CBC",
    "SHA-1": r"hashlib\.sha1\(",
    "ECC-P256": r"ECC\.generate\(curve='P-256'\)"
}

def scan_file(file_path):
    findings = []
    with open(file_path, 'r', errors='ignore') as f:
        content = f.read()
        for label, pattern in RULES.items():
            if re.search(pattern, content):
                findings.append({
                    "file": os.path.basename(file_path),
                    "issue": label,
                    "severity": "High" if "RSA" in label else "Medium"
                })
    return findings
