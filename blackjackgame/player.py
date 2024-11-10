#!/usr/bin/env python3
# Anthony Seng
# CPSC 386-02
# 2023-02-09
# aseng6825@csu.fullerton.edu
# @aseng2
#
# Lab 02-00
#
# This is the Player class and Dealer class
#

"""This is for the player and dealer"""
from blackjackgame.cards import *


def _str_card(c):
    return f"{c.rank} of {c.suit}s"


def _is_ace(c):
    return c.rank == "Ace"


class Player:
    def __init__(self, name, bankroll=10000):
        self._name = name
        self._bankroll = bankroll
        self.cards = []
        self._values = 0
        self._play = True
        self._wager = 0

    def add_card(self, card):
        self.cards.append(card)
        self._values += card_value(card)

    def hand(self):
        print("This is " + self._name + "'s cards: ")
        for c in self.cards:
            print(_str_card(c))
            if _is_ace(c):
                if self._values < 12:
                    self._values += 10
        print(self._values)

    def __str__(self):
        return f"{self._name}"

    def __repr__(self):
        return f"Player({self._name})"

    def hit_or_stand(self, deck):
        x = input("Would you like to hit or stand. Enter h or s: ")

        if x.lower() == "h":
            c1 = deck.deal()
            self.cards.append(c1)
            for c in self.cards:
                if c.rank == "Ace" and self._values < 12:
                    self._values += 10
            self._values += card_value(c1)
            print("You Hit")
        elif x.lower() == "s":
            self._play = False
            print("You Stand")

    def wager(self):
        while True:
            amount = int(input("How much do you want to wager:\n"))
            if amount > self._bankroll:
                print("Please enter an correct amount")
            else:
                self._wager = amount
                break

    def lose_bet(self, amount):
        self._bankroll -= amount

    def win_bet(self, amount):
        self._bankroll += amount

    @property
    def Name(self):
        return self._name

    def bankroll(self):
        return self._bankroll


class Dealer(Player):
    def is_dealer(self):
        return True

    def display(self):
        first = self.cards[0]
        print("This is the Dealer's card: ")
        print(_str_card(first))

    def display_all(self):
        print("This is Dealer's cards: ")
        for c in self.cards:
            print(_str_card(c))
            if c.rank == "Ace" and self._values < 12:
                self._values += 10
        print(self._values)

    def hit(self, deck):
        c1 = deck.deal()
        self.cards.append(c1)
        for c in self.cards:
            if c.rank == "Ace" and self._values < 12:
                self._values += 10
        self._values += card_value(c1)
