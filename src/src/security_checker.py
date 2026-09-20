import re
import sys
from pathlib import Path


SECURITY_PATTERNS = {
    "Use of eval()": r"\beval\s*\(",
    "Use of exec()": r"\bexec\s*\(",
    "Hardcoded password": (
        r"(?i)(password|passwd)\s*=\s*['\"][^'\"]+['\"]"
    ),
    "Possible hardcoded API key": (
        r"(?i)(api[_-]?key|secret[_-]?key)\s*=\s*['\"][^'\"]+['\"]"
    ),
    "Insecure HTTP URL": r"http://[^\s'\"]+",
}


def scan_code(code: str):
    """Scan source code for basic security issues."""
    findings = []

    for name, pattern in SECURITY_PATTERNS.items():
        if re.search(pattern, code):
            findings.append(name)

    return findings


def main():
    if len(sys.argv) != 2:
        print("Usage: python src/security_checker.py <file>")
        sys.exit(1)

    file_path = Path(sys.argv[1])

    if not file_path.exists():
        print(f"File not found: {file_path}")
        sys.exit(1)

    code = file_path.read_text(encoding="utf-8")
    findings = scan_code(code)

    if not findings:
        print("No basic security issues detected.")
        return

    print("Potential security issues found:")

    for finding in findings:
        print(f"- {finding}")


if __name__ == "__main__":
    main()
