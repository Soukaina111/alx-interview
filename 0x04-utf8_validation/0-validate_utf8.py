#!/usr/bin/python3
"""UTF-8 Validation"""

def count_leading_set_bits(number):
    """
    Counts the number of leading set bits (1) in a given number.
    
    Args:
        number (int): The number to check.
    
    Returns:
        int: The number of leading set bits.
    """
    set_bits = 0
    bit_mask = 1 << 7
    while bit_mask & number:
        set_bits += 1
        bit_mask = bit_mask >> 1
    return set_bits


def is_valid_utf8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
        data (list): A list of integers representing the data to be checked.
    
    Returns:
        bool: True if the data is a valid UTF-8 encoding, False otherwise.
    """
    bytes_remaining = 0
    for byte in data:
        if bytes_remaining == 0:
            # Get the number of leading set bits (1) for this byte
            bytes_remaining = count_leading_set_bits(byte)
            
            # 1-byte characters: 0xxxxxxx
            if bytes_remaining == 0:
                continue
            
            # A character in UTF-8 can be 1 to 4 bytes long
            if bytes_remaining == 1 or bytes_remaining > 4:
                return False
        else:
            # Else, this is not the case. Else, this byte is not a full character.
            # Check if the current byte is a valid follow-up byte (a, 10xxxxxx)
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
        bytes_remaining -= 1
    
    # This is for the case where we might not have the complete data for
    # a particular UTF-8 character.
    return bytes_remaining == 0
