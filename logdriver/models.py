from pydantic import BaseModel

class NewLogRequest(BaseModel):
    service: str
    level: str
    payload: dict