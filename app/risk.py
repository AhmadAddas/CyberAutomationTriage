def calculate_risk(results: list[dict]) -> int:
    score = 0

    for result in results:
        if result["malicious"]:
            score += 40

    return min(score, 100)

def get_risk_level(score: int) -> str:
    if score >= 60:
        return "HIGH"

    if score >= 30:
        return "MEDIUM"

    return "LOW"

