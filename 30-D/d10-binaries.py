#!/bin/python3

import math
import os
import random
import re
import sys


def toBaseTwo(n):
    binary = ""
    while n != 0:
        binary_element = str(n % 2)
        binary = binary + binary_element
        n = n // 2

    binary = binary[::-1]
    return binary


def maxOnes(binary):
    split_binary = binary.split("0")
    tally = []
    for partition in split_binary:
        count = partition.count("1")
        tally.append(count)

    sorted_tally = sorted(tally, reverse=True)
    return sorted_tally[0]


if __name__ == '__main__':
    n = int(input().strip())
    binary = toBaseTwo(n)
    output = maxOnes(binary)
    print(output)
