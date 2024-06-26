import math
from typing import Self
from abc import ABCMeta, abstractmethod

from theatrical_players.models.Play import PlayTypeEnum


class PlayCalculator(metaclass=ABCMeta):
    def __init__(self, play_type: PlayTypeEnum):
        self.play_type = play_type

    @abstractmethod
    def calculate_amount(self, audience):
        pass

    @abstractmethod
    def calculate_credits(self, audience):
        pass

    @classmethod
    def of(cls, play_type) -> Self:
        if "comedy" == play_type:
            return ComedyPlayCalculator(play_type)
        elif "tragedy" == play_type:
            return TragedyPlayCalculator(play_type)
        elif "history" == play_type:
            return HistoryPlayCalculator(play_type)
        elif "pastoral" == play_type:
            return PastoralPlayCalculator(play_type)
        else:
            raise ValueError(f'unknown type: {play_type}')


class ComedyPlayCalculator(PlayCalculator):

    def calculate_amount(self, audience):
        this_amount = 30000
        if audience > 20:
            this_amount += 10000 + 500 * (audience - 20)
        return this_amount + 300 * audience

    def calculate_credits(self, audience):
        # add volume credits
        audience_volume_credits = max(audience - 30, 0)
        # add extra credit for every ten comedy attendees
        comedy_volume_credits = math.floor(audience / 5)
        return audience_volume_credits + comedy_volume_credits


class TragedyPlayCalculator(PlayCalculator):
    def calculate_amount(self, audience):
        this_amount = 40000
        if audience > 30:
            this_amount += 1000 * (audience - 30)
        return this_amount

    def calculate_credits(self, audience):
        # add volume credits
        audience_volume_credits = max(audience - 30, 0)
        return audience_volume_credits


class PastoralPlayCalculator(PlayCalculator):
    def calculate_amount(self, audience):
        this_amount = 40000
        if audience > 30:
            this_amount += 1000 * (audience - 30)
        return this_amount

    def calculate_credits(self, audience):
        # add volume credits
        audience_volume_credits = max(audience - 30, 0)
        return audience_volume_credits


class HistoryPlayCalculator(PlayCalculator):
    def calculate_amount(self, audience):
        this_amount = 40000
        if audience > 30:
            this_amount += 1000 * (audience - 30)
        return this_amount

    def calculate_credits(self, audience):
        # add volume credits
        audience_volume_credits = max(audience - 30, 0)
        return audience_volume_credits
