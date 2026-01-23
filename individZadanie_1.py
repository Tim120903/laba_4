# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    print("Enter 10 numbers separated by spaces: ")
    a = list(map(int, input().split()))
    if len(a) != 10:
        print(f"Error: you need to enter exactly 10 numbers!", file=sys.stderr)
        exit(1)

    sum_even = 0
    count_even = 0
    for item in a:
        if item % 2 == 0:
            sum_even += item
            count_even += 1

    print(f"Sum of elements that are multiples of 2: {sum_even}")
    print(f"Number of elements in multiples of 2: {count_even}")
