from app.risk import get_risk_level

def test_high_risk_level() -> None:
    assert get_risk_level(80) == "HIGH"

def test_medium_risk_level() -> None:
    assert get_risk_level(40) == "MEDIUM"

def test_low_risk_level() -> None:
    assert get_risk_level(10) == "LOW"

def test_high_risk_boundary() -> None:
    assert get_risk_level(60) == "HIGH"

def test_medium_risk_boundary() -> None:
    assert get_risk_level(30) == "MEDIUM"
