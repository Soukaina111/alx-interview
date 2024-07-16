#!/usr/bin/python3
"""
This script parses log files and generates statistics on the HTTP status codes and total file size.
"""

import sys
from collections import defaultdict

def parse_log_line(line):
    """
    Parse a single log line and extract the status code and file size.
    """
    data = line.split()
    try:
        status_code = data[-2]
        file_size = int(data[-1])
        return status_code, file_size
    except (IndexError, ValueError):
        return None, None

def update_statistics(status_code, file_size, status_code_counts, total_file_size):
    """
    Update the status code counts and total file size.
    """
    if status_code:
        status_code_counts[status_code] += 1
    if file_size:
        total_file_size += file_size
    return total_file_size

def print_statistics(status_code_counts, total_file_size):
    """
    Print the final statistics.
    """
    print(f"Total file size: {total_file_size}")
    for status_code, count in sorted(status_code_counts.items()):
        if count:
            print(f"{status_code}: {count}")

def main():
    """
    Main function to process log data and generate statistics.
    """
    status_code_counts = defaultdict(int)
    total_file_size = 0
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_log_line(line)
            total_file_size = update_statistics(status_code, file_size, status_code_counts, total_file_size)
            if line_count % 10 == 0:
                print_statistics(status_code_counts, total_file_size)
        print_statistics(status_code_counts, total_file_size)
    except KeyboardInterrupt:
        print_statistics(status_code_counts, total_file_size)
        raise

if __name__ == '__main__':
    main()
