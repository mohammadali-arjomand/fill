#!/usr/bin/python3

from sys import argv

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
print("A" * count)
