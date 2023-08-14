#!/usr/bin/python3

from sys import argv

try:
    count = argv[1]
    if count[-1] == "B":
        count = int(count[:-1])
    elif count[-1] == "K":
        count = int(count[:-1]) * 1024
    elif count[-1] == "M":
        count = int(count[:-1]) * 1024 * 1024
    elif count[-1] == "G":
        count = int(count[:-1]) * 1024 * 1024 * 1024
    elif count[-1] == "T":
        count = int(count[:-1]) * 1024 * 1024 * 1024 * 1024
    else:
        count = int(count)
except:
    print("\033[0;31mBad usage\033[0m")
    print("Who to use? https://github.com/mohammadali-arjomand/fill#usage")
    exit()
print("F" * count)
