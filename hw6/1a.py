n = int(input())
nums = sorted([int(el) for el in input().split()])
k = int(input())
# print(nums)
ans = ['0'] * k

def check(m, num):
    return nums[m] >= num

def rcheck(m, num):
    return nums[m] <= num

def right_binary_search(num):
    left = 0
    right = n - 1
    while left < right:
        m = (left + right + 1) // 2
        if rcheck(m, num):
            left = m
        else:
            right = m - 1
    return left


def left_binary_search(num):
    left = 0
    right = n - 1
    while left < right:
        m = (left + right) // 2
        if check(m, num):
            right = m
        else:
            left = m + 1
    return left


for i in range(k):
    l, r = map(int, input().split())
    left_i = left_binary_search(l)
    right_i = right_binary_search(r)
    # print(left_i, right_i)
    if (left_i == right_i == 0 and nums[0] > r) or (left_i == right_i == (n - 1) and nums[n-1] < l):
        ans[i] = str(0)
    else:
        ans[i] = str(right_i - left_i + 1)
print(" ".join(ans))
