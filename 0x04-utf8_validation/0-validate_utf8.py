#!/usr/bin/python3
""" alx-interview : UTF-8 Validation"""


def count_leading_set_bits(number):
    """
    Counts the number of leading set bits (1) in a given number.

    Args:
        number (int): The number to check.

    Returns:
        int: The number of leading set bits.
    """
    bits = 0
    per = 1 << 7
    while per & number:
        bits += 1
        per = per >> 1
    return bits


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing the data to be checked.

    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    bits_num = 0
    for i in range(len(data)):
        if bits_num == 0:
            bits_num = count_leading_set_bits(data[i])
            if bits_num == 0:
                continue
            if bits_num == 1 or bits_num > 4:
                return False
        else:
            if not (data[i] & (1 << 7) and not (data[i] & (1 << 6))):
                return False
        bits_num -= 1
    return bits_num == 0
