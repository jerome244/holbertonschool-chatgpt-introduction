#!/usr/bin/python3
import sys

# Start from 1 to exclude the script name (sys.argv[0])
for i in range(1, len(sys.argv)):
    print(sys.argv[i])
