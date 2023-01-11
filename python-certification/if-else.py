#!/bin/python3

import math
import os
import random
import re
import sys


def main():
    if (n % 2 == 0):  # if n is even
        if (2 <= n <= 5):
            print("Not Weird")
        if (6 <= n <= 20):
            print("Weird")
        elif (n > 20):
            print("Not Weird")
    else:  # if n is odd
        print("Weird")


if __name__ == '__main__':
    n = int(input().strip())
    main()
