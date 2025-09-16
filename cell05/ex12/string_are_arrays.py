#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]

    if 'z' not in input_string:
        print("none")
    else:
        z_count = input_string.count('z')

        print("z"*z_count)