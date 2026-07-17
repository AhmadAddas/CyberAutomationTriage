import json
from pathlib import Path
from typing import Any

def load_threat_intel() -> dict[str, Any]:
    path = Path("data/threat_intel.json")
    with path.open("r",encoding="utf-8") as file:
        return json.load(file)

def lookup_indicator(indicator: str) -> dict:
    threat_intel = load_threat_intel()

    result = threat_intel.get(indicator)

    if result is None:
        return {
            "indicator": indicator,
            "found": False,
            "malicious": False,
            "confidence": 0,
            "tags": [],
        }
    return {
        "indicator": indicator,
        "found": True,
        "malicious": result["malicious"],
        "confidence": result["confidence"],
        "tags": result["tags"],
    }
