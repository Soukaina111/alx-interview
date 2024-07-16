#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics:
"""


import sys
import re

# Initialize variables
total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

def parse_line(line):
    match = re.match(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[(.*?)\] "(GET \/projects\/[0-9]+ HTTP\/1\.1)" (\d+) (\d+)', line)
    if match:
        ip_address, timestamp, status_code, file_size = match.groups()
        global total_file_size
        total_file_size += int(file_size)
        if status_code in status_code_counts:
            status_code_counts[int(status_code)] += 1

try:
    for line in sys.stdin:
        parse_line(line)

        # Check if we've processed 10 lines or CTRL+C was pressed
        if len(sys.stdin) % 10 == 0 or sys.stdin.closed:
            print(f'Total file size: {total_file_size}')
            for status_code, count in sorted(status_code_counts.items()):
                if count > 0:
                    print(f'{status_code}: {count}')
            # Reset counters for next batch
            total_file_size = 0
            status_code_counts = {code: 0 for code in status_code_counts}
except KeyboardInterrupt:
    print(f'\nTotal file size: {total_file_size}')
    for status_code, count in sorted(status_code_counts.items()):
        if count > 0:
            print(f'{status_code}: {count}')

