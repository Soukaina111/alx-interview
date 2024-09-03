#!/usr/bin/python3
"""Module for Prime Game"""

def isWinner(x, nums):
    """
    Determines the winner of a series of prime number removal games.

    Args:
        x (int): The total number of rounds.
        nums (list of int): A list of integers where each integer n signifies
        a set of consecutive integers from 1 to n.

    Returns:
        str: The name of the player who won the most rounds (either "Ben"
        or "Maria").
        None: If the winner cannot be determined.

    Raises:
        None.
    """
    # Validate input parameters
    if x <= 0 or nums is None:  # Check if there are valid rounds and nums is not empty
        return None
    if x != len(nums):  # Ensure the count of rounds matches the length of nums
        return None
    
    # Initialize scores for both players
    ben = 0
    maria = 0
    
    # Create a list 'a' with length equal to the highest number in nums + 1,
    # initially assuming all numbers are prime
    a = [1 for _ in range(sorted(nums)[-1] + 1)]
    
    # Set the first two elements of the list to 0 since 0 and 1 are not prime
    a[0], a[1] = 0, 0
    
    # Implement the Sieve of Eratosthenes to identify prime numbers
    i = 2
    while i < len(a):  # Use a while loop to iterate through each number
        rm_multiples(a, i)  # Remove multiples of the current prime number
        i += 1  # Move to the next number

    # Play each round based on the numbers provided
    round_index = 0
    while round_index < len(nums):  # Iterate through each number in nums
        n = nums[round_index]  # Get the current number
        # If the sum of primes in the range is even, Ben wins this round
        if sum(a[0:n + 1]) % 2 == 0:
            ben += 1  # Increment Ben's score
        else:
            maria += 1  # Increment Maria's score
        round_index += 1  # Move to the next round

    # Determine who has won the most rounds
    if ben > maria:  # Check if Ben has more wins
        return "Ben"
    if maria > ben:  # Check if Maria has more wins
        return "Maria"
    return None  # Return None if there's a tie

def rm_multiples(ls, x):
    """
    Marks multiples of a given prime number as non-prime in an array.

    Args:
        ls (list of int): An array representing potential prime numbers.
        x (int): The prime number whose multiples need to be marked.

    Returns:
        None.

    Raises:
        None.
    """
    # This loop marks all multiples of a prime number as non-prime by
    # setting their corresponding values to 0 in the provided list.
    
    i = 2
    while i < len(ls):  # Use a while loop to check multiples of x
        try:
            ls[i * x] = 0  # Mark the multiple as non-prime
        except (ValueError, IndexError):  # Handle out-of-bounds errors
            break  # Exit the loop if the index goes out of range
        i += 1  # Increment i to check the next multiple