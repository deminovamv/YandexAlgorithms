def l_bin_search(left, right, check):
    while left < right:
        m = (left + right) // 2
        # print(m)
        # print(check(m))
        if check(m):
            right = m
        else:
            left = m + 1
    return left


a, k, b, m, x = map(int, input().split())


def trees_cut(days):
    return a * (days - days // k) + b * (days - days // m)

def check(days):
    return trees_cut(days) >= x


print(l_bin_search(0, x, check))
