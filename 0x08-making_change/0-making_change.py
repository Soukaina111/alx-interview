#!/usr/bin/python3
""" This script provides a function to generate the changes
needed to reach a given total amount,
    using a list of available coins.
"""


def makeChange(coins, total):
    """ Generate changes needed to reach total

    Args:
        coins (List): List of Coins available
        total (int): Total amount needed
    """
    # If the total is less than or equal to 0, no coins are needed
    if total <= 0:
        return 0

    verf = 0
    axe  = 0

    # Sort the coins in descending order to use the largest coins first
    coins.sort(reverse=True)

   
    for i in coins:
        while verf < total:
            verf += i
            axe += 1
        if verf == total:
            return axe
        verf -= i
        axe -= 1
    return -1