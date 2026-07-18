def get_recommended_action(risk_level: str) -> str:
    if risk_level == "HIGH":
        return "Escalate for immediate analyst review"

    if risk_level == "MEDIUM":
        return "Queue for analyst investigation"

    return "Monitor and close if no additional evidence is found"

def build_report(
    alert: dict,
    results: list[dict],
    score: int,
    risk_level: str,
) -> dict:
    findings = []

    for result in results:
        if result["malicious"]:
            findings.append(
                f"{result['indicator']} was identified as malicious"
            )


    return {
        "alert_id": alert["alert_id"],
        "risk_score": score,
        "risk_level": risk_level,
        "indicators": results,
        "findings": findings,
        "recommended_action": get_recommended_action(risk_level),
    }
