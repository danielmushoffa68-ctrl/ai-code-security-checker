from src.security_checker import scan_code


def test_detect_eval():
    findings = scan_code("result = eval(user_input)")
    assert "Use of eval()" in findings


def test_detect_hardcoded_password():
    findings = scan_code('password = "secret123"')
    assert "Hardcoded password" in findings


def test_detect_insecure_http():
    findings = scan_code('url = "http://example.com"')
    assert "Insecure HTTP URL" in findings


def test_safe_code():
    findings = scan_code("total = price * quantity")
    assert findings == []
