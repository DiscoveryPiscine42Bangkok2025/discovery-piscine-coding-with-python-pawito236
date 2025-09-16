#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    command_line_param = sys.argv[1]
    user_input = input("What was the parameter? ")
    if user_input == command_line_param:
        print("Good job!")
    else:
        print("Nope, sorry...")