#!/usr/bin/python3
import sys
if __name__ == "__main__":
    count = len(sys.argv) -1
    if count = 0:
        print("0 arguments.")
    elif count = 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(len(sys.argv) -1):
        print("{}: {}".format(i + 1, sys.argv[index + 1]))
