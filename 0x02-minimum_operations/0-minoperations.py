#!/usr/bin/python3
""" Alx -interview Minimum Operations
    """


def minOperations(n):
    if n <= 0:
        return 0

    # set the number of operations to 0
    opera = 0

    # While the current number of 'H' is less than 'n'
    while n > 1:
        # If 'n' is divisible by 2, we can copy-paste to x2 the number of 'H'
        if n % 2 == 0:
            n //= 2
            opera += 1
        # if not , we need to copy and paste one more 'H'
        else:
            n -= 1
            opera += 2

    # finally the last operation is to copy and paste the remaining 'H'
    return opera + 1
