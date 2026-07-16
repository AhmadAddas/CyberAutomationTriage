import json
from pathlib import Path
from typing import Any


def load_alert(path: str) -> dict[str, Any]:
    alert_path = Path(path)

    with alert_path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> None:
    alert = load_alert("examples/alert.json")

    print(f"Alert ID: {alert['alert_id']}")
    print(f"Source IP: {alert['source_ip']}")
    print(f"Domain: {alert['domain']}")


if __name__ == "__main__":
    main()
