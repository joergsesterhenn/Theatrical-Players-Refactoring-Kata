from pydantic import BaseModel


class Performance(BaseModel):
    playID: str
    audience: int
