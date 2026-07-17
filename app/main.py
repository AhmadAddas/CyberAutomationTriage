import json
from pathlib import Path
from typing import Any
from app.intel import lookup_indicator
from app.risk import calculate_risk
from app.risk import get_risk_level

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
