#!/usr/bin/env python3
"""
Log parsing script that reads from stdin, processes log entries,
and prints statistics about file sizes and HTTP status codes.
"""

import sys


def main():
    """
    Main function to handle log parsing and statistics computation.
    """
    total_file_size, line_count = 0, 0
    http_status_codes = ["200", "301", "400", "401",
            "403", "404", "405", "500"]
    status_code_counts = {code: 0 for code in http_status_codes}

    def display_statistics(total_file_size: int, status_code_counts: dict) -> None:
        """
        Displays the current statistics about total file size and status code counts.
        """
        print(f"Total file size: {total_file_size}")
        for status_code, count in sorted(status_code_counts.items()):
            if count > 0:
                print(f"{status_code}: {count}")

    try:
        for line in sys.stdin:
            line_count += 1
            log_entries = line.split()

            try:
                extracted_status_code = log_entries[-2]
                if extracted_status_code in status_code_counts:
                    status_code_counts[extracted_status_code] += 1
            except Exception as e:
                print(f"Error extracting status code: {e}", file=sys.stderr)

            try:
                total_file_size += int(log_entries[-1])
            except Exception as e:
                print(f"Error updating total file size: {e}", file=sys.stderr)

            if line_count % 10 == 0 or sys.stdin.closed:
                display_statistics(total_file_size, status_code_counts)
                
        display_statistics(total_file_size, status_code_counts)
    except KeyboardInterrupt:
        print("\nStatistics up to the last full set of 10 lines:")
        display_statistics(total_file_size, status_code_counts)
        print("\nOperation interrupted by user.")
        raise


if __name__ == "__main__":
    main()
