#!/usr/bin/python3
"""
Log parsing
"""

import sys

if __name__ == '__main__':

    file_size, count = 0, 0
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    stats = {k: 0 for k in codes}

    def print_stats(stats: dict, file_size: int) -> None:
        """Prints the accumulated metrics."""
        print("File size: {:d}".format(file_size))
        for k in sorted(stats.keys()):
            if stats[k]:
                print("{}: {}".format(k, stats[k]))

    try:
        for line in sys.stdin:
            count += 1
            try:
                # Split line into components
                data = line.split()
                
                # Validate and extract components of the log line
                if len(data) < 7:
                    continue

                # Extract status code and file size
                status_code = data[-2]
                file_size_part = int(data[-1])

                # Update status code count if valid
                if status_code in stats:
                    stats[status_code] += 1

                # Update total file size
                file_size += file_size_part

            except (ValueError, IndexError):
                # Skip lines that don't match the expected format
                continue

            # Print stats every 10 lines
            if count % 10 == 0:
                print_stats(stats, file_size)

        # Print final stats after reading all input
        print_stats(stats, file_size)

    except KeyboardInterrupt:
        # Print stats on keyboard interrupt
        print_stats(stats, file_size)
        raise
