# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
        a = list(map(float, input().split()))

        if not a:
            print("The specified list is empty", file=sys.stderr)
            exit(1)

        count_pos = 0
        for num in a:
            if num > 0:
                count_pos += 1

        last_zero_index = -1
        for i in range(len(a) - 1, -1, -1):
            if a[i] == 0:
                last_zero_index = i
                break

        sum_after_zero = 0
        if last_zero_index != -1 and last_zero_index < len(a) - 1:
            # Берем срез списка после последнего нуля
            after_zero = a[last_zero_index + 1:]
            for num in after_zero:
                sum_after_zero += num
        elif last_zero_index == -1:
            for num in a:
                sum_after_zero += num

        print(f"The number of positive elements: {count_pos}")
        print(f"The sum of the elements after the last zero: {sum_after_zero}")
