import json
from pathlib import Path
from typing import Any
from app.intel import lookup_indicator
from app.risk import calculate_risk
from app.risk import get_risk_level
from app.models import Alert
from app.report import build_report

from fastapi import FastAPI

app = FastAPI(
    title="Cyber Automation Triage API",
    version="1.0.0",
)

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/analyze")
def analyze_alert(alert: Alert):
    alert_data = alert.model_dump()

    results = [
        lookup_indicator(alert.source_ip),
        lookup_indicator(alert.domain),
    ]

    score = calculate_risk(results)

    risk_level = get_risk_level(score)

    report = build_report(
        alert=alert_data,
        results=results,
        score=score,
        risk_level=risk_level,
    )

    return report


print()


def load_alert(path: str) -> dict[str, Any]:
    alert_path = Path(path)

    with alert_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    alert = load_alert("examples/alert.json")
    print()
    print(f"Alert ID: {alert['alert_id']}")
    print(f"Source IP: {alert['source_ip']}")
    print(f"Domain: {alert['domain']}")
    print()

    lookup_indicator(alert["source_ip"])
    print()

    ip_result = lookup_indicator(alert["source_ip"])
    domain_result = lookup_indicator(alert["domain"])
    print(ip_result)
    print(domain_result)

    print()
    print()
    print("######RESULTS DUPLICATE TEST######")
    print()

    results = [
     lookup_indicator(alert["source_ip"]),
     lookup_indicator(alert["domain"]),
    ]

    for result in results:
        print(result)

    print()

    print("Score")
    score = calculate_risk(results)
    risk_level = get_risk_level(score)

    print(f"Risk score: {score}")
    print(f"Risk level: {risk_level}")

    print()

if __name__ == "__main__":
    main()
