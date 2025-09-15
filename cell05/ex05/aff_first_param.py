#!/usr/bin/env python3

import sys

# Check the number of arguments passed to the script
if len(sys.argv) > 1:
    # If there is at least one parameter, print the first one
    print(sys.argv[1])
else:
    # If there are no parameters, print "none"
    print("none")