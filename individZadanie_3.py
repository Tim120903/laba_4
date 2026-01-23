# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    power = tuple(map(int, input("Powers (30 numbers): ").split()))
    price = tuple(map(int, input("Cost (30 numbers): ").split()))

    if len(power) != 30 or len(price) != 30:
        print("You need exactly 30 values.", file=sys.stderr)
        exit(1)

    count = 0
    print("Car prices ≤ 80 horsepower:")
    for pwr, prc in zip(power, price):
        if pwr <= 80:
            print(f"{prc} k.$")
            count += 1

    print(f"Total found: {count} cars")