from enum import Enum

from pydantic import BaseModel, RootModel


class PlayTypeEnum(str, Enum):
    comedy = 'comedy'
    tragedy = 'tragedy'
    historic = 'history'
    pastoral = 'pastoral'
    popular_comedy = 'popular-comedy'


class Play(BaseModel):
    name: str
    type: PlayTypeEnum


class Plays(RootModel):
    """
    Plays can be provided as JSON Object
    {
      "hamlet": {"name": "Hamlet", "type": "tragedy"},
      "as-like": {"name": "As You Like It", "type": "comedy"},
      "othello": {"name": "Othello", "type": "tragedy"}
     }
    """
    root: dict[str, Play]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]
