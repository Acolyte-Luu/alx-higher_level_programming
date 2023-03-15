#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    for index in range(len(sys.argv) - 1):
        total += int(sys.argv[index + 1])
    print("{}".format(total))
