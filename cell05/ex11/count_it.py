#!/usr/bin/env python3

import sys

params = sys.argv[1:]
num_params = len(params)

if num_params == 0:
    print("none")
else:
    print(f"parameters: {num_params}")

    for param in params:
        print(f"{param}: {len(param)}")