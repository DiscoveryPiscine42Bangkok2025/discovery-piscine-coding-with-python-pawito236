#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
else:
    keyword = sys.argv[1]
    search_string = sys.argv[2]

    if keyword not in search_string:
        print("none")
    else:
        count = search_string.count(keyword)
        print(count)