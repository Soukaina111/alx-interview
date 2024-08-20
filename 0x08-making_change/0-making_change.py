#!/usr/bin/python3
""" This script provides a function to generate the changes needed to reach a given total amount,
    using a list of available coins.
"""


def makeChange(coins, total):
    """ Generate changes needed to reach total

    This function takes a list of coins and a total amount as input, and returns the minimum
    number of coins needed to make the total amount. If the total cannot be reached, it returns -1.

    Args:
        coins (List): List of Coins available
        total (int): Total amount needed
    """
    # If the total is less than or equal to 0, no coins are needed
    if total <= 0:
        return 0

    # Initialize variables to keep track of the current check amount and the number of coins used
    verf = 0
    axe  = 0

    # Sort the coins in descending order to use the largest coins first
    coins.sort(reverse=True)

    # Iterate through the coins, adding them to the current check amount until the total is reached
    for i in coins:
        while verf < total:
            verf += i
            axe += 1
        # If the current check amount is equal to the total, return the number of coins used
        if verf == total:
            return axe
        # If the current check amount is greater than the total, subtract the last coin and decrement the number of coins used
        verf -= i
        axe -= 1

    # If the total cannot be reached with the available coins, return -1
    return -1