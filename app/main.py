from pathlib import Path
import json

def main() -> None:
    alert_path = Path("examples/alert.json")

    with alert_path.open("r", encoding="utf-8") as file:
        alert = json.load(file)
    print()
    print("====JSON====")
    print(alert)
    print("============")
    print()
    print("==Objects===")
    print(alert["alert_id"])
    print(alert["source_ip"])
    print(alert["domain"])
    print("============")
    print()

if __name__ == "__main__":
    main()
