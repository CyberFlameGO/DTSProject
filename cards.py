#!/usr/bin/env python3.10
"""
card stuff
"""
import random as rand


def generate_cards(min_range: int, max_range: int, amount_of_each: int) -> tuple[dict, list]:
    """
    TODO: Potentially switch amount_of_each to char of c,h,d,s
    !!! hhh the teacher had a wayyy better way of doing this
    Generate cards
    :rtype: tuple[dict, list]
    :param min_range:
    :param max_range:
    :param amount_of_each:
    :return:
    """
    cards_kv: dict[int, int] = {}
    max_range += 1
    for i in range(min_range, max_range):
        cards_kv[i]: dict = amount_of_each
    cards_k: list = list(cards_kv.keys())
    rand.shuffle(cards_k)
    return cards_kv, cards_k


running: bool = True
while running:
    cd, cl = generate_cards(1,16,4)
