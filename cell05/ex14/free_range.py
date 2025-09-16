#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    try:
        start_num = int(sys.argv[1])
        end_num = int(sys.argv[2])

        number_list = list(range(start_num, end_num + 1))
        print(number_list)
        
    except ValueError:
        print("none")