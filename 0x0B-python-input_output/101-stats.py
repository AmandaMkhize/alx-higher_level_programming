#!/usr/bin/python3
import sys

def print_metrics(total_size, status_counts):
    print("File size: {}".format(total_size))
    for status_code in sorted(status_counts.keys()):
        print("{}: {}".format(status_code, status_counts[status_code]))

def main():
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            ip, _, _, status_code, file_size = line.strip().split(" ", 4)
            total_size += int(file_size)
            status_counts[status_code] = status_counts.get(status_code, 0) + 1

            if i % 10 == 0:
                print_metrics(total_size, status_counts)
                total_size = 0
                status_counts = {}
    except KeyboardInterrupt:
        print_metrics(total_size, status_counts)

if __name__ == "__main__":
    main()
