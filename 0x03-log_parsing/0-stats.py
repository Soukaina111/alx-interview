#!/usr/bin/python3
"""
This script parses log files and generates statistics on the HTTP status codes and total file size.
"""

import sys

if __name__ == '__main__':
    # Initialize variables to track file size and count of lines processed
    filesize, count = 0, 0

    # Define a list of HTTP status codes to track
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]

    # Create a dictionary to store the count of each status code
    stats = {k: 0 for k in codes}

    # Define a function to print the final statistics
    def print_stats(stats: dict, file_size: int) -> None:
        print("File size: {:d}".format(filesize))
        for k, v in sorted(stats.items()):
            if v:
                print("{}: {}".format(k, v))

    try:
        # Process each line from stdin
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                # Extract the HTTP status code from the log line
                status_code = data[-2]
                if status_code in stats:
                    # Increment the count for the corresponding status code
                    stats[status_code] += 1
            except BaseException:
                # Ignore any errors parsing the status code
                pass
            try:
                # Extract the file size from the log line and add it to the total
                filesize += int(data[-1])
            except BaseException:
                # Ignore any errors parsing the file size
                pass
            # Print the statistics every 10 lines
            if count % 10 == 0:
                print_stats(stats, filesize)
        # Print the final statistics
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        # Print the statistics and exit if the user interrupts the script
        print_stats(stats, filesize)
        raise
