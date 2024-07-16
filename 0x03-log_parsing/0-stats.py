#!/usr/bin/python3
"""
This script parses log files and generates statistics on the HTTP status codes and total file size.
"""

import sys

if __name__ == '__main__':
    # Initialize variables to track total file size and count of lines processed
    total_file_size, line_count = 0, 0

    # Define a list of HTTP status codes to track
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]

    # Create a dictionary to store the count of each status code
    status_code_counts = {code: 0 for code in status_codes}

    # Define a function to print the final statistics
    def print_statistics(status_code_counts: dict, total_file_size: int) -> None:
        print("Total file size: {:d}".format(total_file_size))
        for code, count in sorted(status_code_counts.items()):
            if count:
                print("{}: {}".format(code, count))

    try:
        # Process each line from stdin
        for line in sys.stdin:
            line_count += 1
            data = line.split()
            try:
                # Extract the HTTP status code from the log line
                status_code = data[-2]
                if status_code in status_code_counts:
                    # Increment the count for the corresponding status code
                    status_code_counts[status_code] += 1
            except BaseException:
                # Ignore any errors parsing the status code
                pass
            try:
                # Extract the file size from the log line and add it to the total
                file_size = int(data[-1])
                total_file_size += file_size
            except BaseException:
                # Ignore any errors parsing the file size
                pass
            # Print the statistics every 10 lines
            if line_count % 10 == 0:
                print_statistics(status_code_counts, total_file_size)
        # Print the final statistics
        print_statistics(status_code_counts, total_file_size)
    except KeyboardInterrupt:
        # Print the statistics and exit if the user interrupts the script
        print_statistics(status_code_counts, total_file_size)
        raise
