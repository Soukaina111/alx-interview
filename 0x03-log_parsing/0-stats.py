#!/usr/bin/python3
"""
Log parsing script that reads from stdin, processes log entries, and prints statistics about file sizes and HTTP status codes.
"""

import sys

def main():
    """
    Main function to handle log parsing and statistics computation.
    """
    # Initialize variables for tracking file size and status code counts
    filesize, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]  # List of valid status codes
    stats = {k: 0 for k in codes}  # Dictionary to hold counts of each status code

    def print_stats(stats: dict, file_size: int) -> None:
        """
        Prints the current statistics about file sizes and status codes.
        """
        print("File size:", file_size)
        for k, v in sorted(stats.items()):
            if v:
                print(f"{k}: {v}")

    try:
        # Process each line from stdin
        for line in sys.stdin:
            count += 1
            data = line.split()

            # Attempt to extract and increment the status code count
            try:
                status_code = data[-2]
                if status_code in stats:
                    stats[status_code] += 1
            except Exception as e:
                print(f"Error extracting status code: {e}", file=sys.stderr)

            # Attempt to extract and increment the file size
            try:
                filesize += int(data[-1])
            except Exception as e:
                print(f"Error converting file size: {e}", file=sys.stderr)

            # Print statistics every 10 lines
            if count % 10 == 0:
                print_stats(stats, filesize)
                
        # Ensure final statistics are printed
        print_stats(stats, filesize)
    except KeyboardInterrupt:
        print("\nStatistics up to the last full set of 10 lines:")
        print_stats(stats, filesize)
        print("\nInterrupted by user.")
        raise

if __name__ == '__main__':
    main()

