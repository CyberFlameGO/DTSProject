#!/usr/bin/env python3.10
"""
card stuff
"""
cards: dict = {}


def generate_cards(min_range: int, max_range: int, amount_of_each: int):
    """

    :param min_range:
    :param max_range:
    :param amount_of_each:
    """
    global cards
    cards: dict = {}
    for i in range(min_range, max_range):
        cards[i] = amount_of_each
