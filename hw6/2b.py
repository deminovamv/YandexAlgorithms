"""
Требуется определить в заданном массиве номер самого левого и самого правого элемента, равного искомому числу.
"""

n = int(input())
nums_n = [int(el) for el in input().split()]
m = int(input())
nums_m = [int(el) for el in input().split()]


def check(m, num):
    return nums_n[m] >= num


def rcheck(m, num):
    return nums_n[m] <= num


def left_binary_search(num):
    left = 0
    right = n - 1
    while left < right:
        m = (left + right) // 2
        if check(m, num):
            right = m
        else:
            left = m + 1
    if nums_n[left] != num:
        return 0
    return left + 1


def right_binary_search(num):
    left = 0
    right = n - 1
    while left < right:
        m = (left + right + 1) // 2
        if rcheck(m, num):
            left = m
        else:
            right = m - 1
    if nums_n[left] != num:
        return 0
    return left + 1


for el in nums_m:
    print(left_binary_search(el), right_binary_search(el))
