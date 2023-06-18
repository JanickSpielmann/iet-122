#!/usr/bin/python3
import sys

# Accessing parameters
script_name = sys.argv[0]
arguments = sys.argv[1:]

# Printing script name
print("Script name:", script_name)

# Printing arguments
if arguments:
    print("Arguments:")
    for arg in arguments:
        print(arg)
else:
    print("No arguments provided.")