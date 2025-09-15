#!/usr/bin/env python3

original_array = [2, 8, 9, 48, 8, 22, -12, 2]

processed_values = [number + 2 for number in original_array if number > 5]
result_set = set(processed_values)

print(original_array)
print(result_set)