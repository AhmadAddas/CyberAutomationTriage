from pydantic import BaseModel


class Alert(BaseModel):
    alert_id: str
    source_ip: str
    domain: str
