#!/usr/bin/env python3
# Anthony Seng
# CPSC 386-02
# 2023-02-16
# aseng6825@csu.fullerton.edu
# @aseng2
#
# Lab 02-00
#
# game.py
#

"""This is the game file for blackjack"""
from blackjackgame.cards import *
from blackjackgame.player import *
from random import randint
import os
import os.path
import pickle
import locale


def _str_card(c):
    return f"{c.rank} of {c.suit}s"


class blackjack:
    def __init__(self):
        print("Welcome to BlackJack")

    def run(self):
        from time import sleep

        # playing = True
        # while playing:
        # num_players = int(input("How many players?\n"))
        # player_list = []
        num_players = 0
        player_list = []
        main_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(main_dir, "data")
        pickle_file = os.path.join(data_dir, "players.pk1")
        # locale.setlocale(locale.LC_ALL, "en_US") # Are you a new player?
        new_players = input("Are you a new player?\n")
        if new_players.lower() == "n":
            if os.path.exists(pickle_file):
                with open(pickle_file, "rb") as fh:
                    player_list = pickle.load(fh)
                num_players = len(player_list)
        if new_players.lower() == "y":
            num_players = int(input("How many players? "))
            for _ in range(num_players):
                x = input("What is your name?\n")
                player_list.append(Player(x))
        print("We made the following players: ")
        for player in player_list:
            print(f"{player} has {player._bankroll}")

        # for _ in range(num_players):
        # x = input("What is your name?\n")
        # player_list.append(Player(x))

        dealer = Dealer("dealer")
        while True:
            # bet = input("How much do you want to bet:\n")
            d = Deck()
            for _ in range(7):
                w = Deck()
                d.merge(w)
            d.shuffle()
            d.cut()
            for player in player_list:
                print(player.__repr__())
                # wagers = int(input("How much do you want to wager:\n"))
                player.wager()
            for player in player_list:
                c1 = d.deal()
                c2 = d.deal()
                player.add_card(c1)
                player.add_card(c2)
                print(player.__repr__())
                player.hand()

            c3 = d.deal()
            c4 = d.deal()

            dealer.add_card(c3)
            dealer.add_card(c4)
            dealer.display()

            for player in player_list:
                while player._play:
                    print(player.__repr__())
                    player.hit_or_stand(d)
                    player.hand()
                    if player._values > 21:
                        print("Player " + player.__str__() + " bust")
                        x = player._wager
                        player.lose_bet(x)
                        print(player.__repr__())
                        print(player._bankroll)
                        break

            for player in player_list:
                if player._values <= 21:
                    while dealer._values < 17:
                        dealer.hit(d)
                    if dealer._values > 21:
                        print("Dealer Bust")
                        x = player._wager
                        player.win_bet(x)
                        dealer.display_all()
                        print(player.__repr__())
                        print(player._bankroll)
                    elif dealer._values > player._values:
                        print("Dealer wins")
                        x = player._wager
                        player.lose_bet(x)
                        dealer.display_all()
                        print(player.__repr__())
                        print(player._bankroll)
                    elif dealer._values <= player._values:
                        print("Player wins")
                        x = player._wager
                        player.win_bet(x)
                        dealer.display_all()
                        print(player.__repr__())
                        print(player._bankroll)

            new_game = input(
                "Would you like to play another game? Enter y or n \n"
            )

            if new_game.lower() == "y":
                for player in player_list:
                    player._play = True
                    player._values = 0
                    player._wager = 0
                    player.cards = []
                    dealer.cards = []
                    dealer._values = 0

            elif new_game.lower() == "n":
                for player in player_list:
                    player._play = True
                print("Thanks for playing")
                if not os.path.exists(data_dir):
                    os.mkdir(data_dir)
                with open(pickle_file, "wb") as fh:
                    pickle.dump(player_list, fh, pickle.HIGHEST_PROTOCOL)
                break
