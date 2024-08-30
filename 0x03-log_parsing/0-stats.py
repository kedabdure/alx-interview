#!/usr/bin/python3
"""
Log parsing script to read stdin line by line and compute metrics.
"""

import sys

def print_stats(stats: dict, total_size: int) -> None:
    """Prints the accumulated metrics."""
    print("File size: {:d}".format(total_size))
    for code in sorted(stats.keys()):
        if stats[code] > 0:
            print("{}: {}".format(code, stats[code]))

def main():
    total_size = 0
    line_count = 0
    status_codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {code: 0 for code in status_codes}

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            
            # Validate line format and extract necessary parts
            if len(parts) >= 7:
                status_code = parts[-2]
                try:
                    file_size = int(parts[-1])
                    total_size += file_size
                except ValueError:
                    continue

                if status_code in stats:
                    stats[status_code] += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats(stats, total_size)

        # Print final stats after processing all input
        print_stats(stats, total_size)

    except KeyboardInterrupt:
        # Print stats on keyboard interrupt
        print_stats(stats, total_size)
        raise

if __name__ == "__main__":
    main()
