from pydantic import BaseModel

from theatrical_players.models.Performance import Performance


class Invoice(BaseModel):
    customer: str
    performances: list[Performance]

