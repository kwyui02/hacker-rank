#!/bin/python3

import math
import os
import random
import re
import sys


def getHourglassSum(matrix, row, column):
    sum = 0
    sum += matrix[row - 1][column - 1]
    sum += matrix[row - 1][column]
    sum += matrix[row - 1][column + 1]
    sum += matrix[row][column]
    sum += matrix[row + 1][column - 1]
    sum += matrix[row + 1][column]
    sum += matrix[row + 1][column + 1]
    return sum


def main(matrix):
    max_hourglass_sum = -63
    for i in range(1, 5):
        for j in range(1, 5):
            current_hourglass_sum = getHourglassSum(matrix, i, j)
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum
    return max_hourglass_sum


if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    print(main(arr))
