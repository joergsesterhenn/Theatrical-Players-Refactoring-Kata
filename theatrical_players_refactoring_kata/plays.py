import math
from typing import Self
from abc import ABCMeta, abstractmethod


class Play(metaclass=ABCMeta):
    def __init__(self, play_type, play_name):
        self.play_type = play_type
        self.play_name = play_name

    @abstractmethod
    def calculate_amount(self, audience):
        pass

    @abstractmethod
    def calculate_credits(self, audience):
        pass

    @classmethod
    def of(cls, play_type, play_name) -> Self:
        if "comedy" == play_type:
            return ComedyPlay(play_type, play_name)
        elif "tragedy" == play_type:
            return TragedyPlay(play_type, play_name)
        else:
            raise ValueError(f'unknown type: {play_type}')


class ComedyPlay(Play):

    def calculate_amount(self, audience):
        this_amount = 30000
        if audience > 20:
            this_amount += 10000 + 500 * (audience - 20)
        this_amount += 300 * audience
        return this_amount

    def calculate_credits(self, audience):
        # add volume credits
        audience_volume_credits = max(audience - 30, 0)
        # add extra credit for every ten comedy attendees
        comedy_volume_credits = math.floor(audience / 5)
        return audience_volume_credits + comedy_volume_credits


class TragedyPlay(Play):
    def calculate_amount(self, audience):
        this_amount = 40000
        if audience > 30:
            this_amount += 1000 * (audience - 30)
        return this_amount

    def calculate_credits(self, audience):
        # add volume credits
        audience_volume_credits = max(audience - 30, 0)
        return audience_volume_credits
