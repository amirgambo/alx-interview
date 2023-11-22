#!/usr/bin/python3
"""
Calculates least number of coins required for an amount
"""


def makeChange(coins, total):
    """
    Calculates amount of change to be given with least number of coins
    """
    if total <= 0:
        return 0
    remainder = total
    coin_counter = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while remainder > 0:
        if coin_index >= n:
            return -1
        if remainder - sorted_coins[coin_index] >= 0:
            remainder -= sorted_coins[coin_index]
            coin_counter += 1
        else:
            coin_index += 1
    return coin_counter
