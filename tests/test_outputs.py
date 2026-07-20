import json
from pathlib import Path

def test_report_exists():
    """1. The agent produced a JSON report file at `/app/report.json`."""
    assert Path("/app/report.json").exists(), "no report.json found"

def test_total_requests():
    """2. The report contains the correct "total_requests"."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data.get("total_requests") == 6, "incorrect total_requests"

def test_unique_ips():
    """3. The report contains the correct "unique_ips"."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data.get("unique_ips") == 3, "incorrect unique_ips"

def test_top_path():
    """4. The report contains the correct "top_path"."""
    data = json.loads(Path("/app/report.json").read_text())
    assert data.get("top_path") == "/index.html", "incorrect top_path"
