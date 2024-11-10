#!/usr/bin/env python3
# Anthony Seng
# CPSC 386-02
# 2023-02-16
# aseng6825@csu.fullerton.edu
# @aseng2
#
# Lab 02-00
#
# cards.py
#

"""This it the cards file for blackjack"""

from collections import namedtuple
from random import shuffle, randrange
import random
from math import ceil

Card = namedtuple("Card", ["rank", "suit"])


def _str_card(c):
    return f"{c.rank} of {c.suit}s"


def _is_ace(c):
    return c.rank == "Ace"


class Deck:
    ranks = ["Ace"] + [str(x) for x in range(2, 11)] + "Jack Queen King".split()
    suits = "Club Heart Spade Diamond".split()
    values = list(range(1, 11)) + [10, 10, 10]
    values_dict = dict(zip(ranks, values))

    def __init__(self):
        self._cards = [
            Card(rank, suit) for suit in self.suits for rank in self.ranks
        ]

    def cut(self):
        extra = ceil(len(self._cards) * 0.2)
        half = (len(self._cards) // 2) + randrange(-extra, extra)
        tophalf = self._cards[:half]
        bottomhalf = self._cards[half:]
        self._cards = bottomhalf + tophalf

    def shuffle(self):
        random.shuffle(self._cards)

    def deal(self):
        return self._cards.pop()

    def merge(self, other_deck):
        self._cards = self._cards + other_deck._cards


def card_value(c):
    return Deck.values_dict[c.rank]
