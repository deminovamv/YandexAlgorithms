n = int(input())
array = [int(elem) for elem in input().split()]
pref_sum = [0] * (n + 1)
max_sum = array[0]
min_pref_sum_i = 0
max_pref_sum_i = 0
diff = 0
for i in range(1, n + 1):
    pref_sum[i] = pref_sum[i - 1] + array[i - 1]

    if pref_sum[i - 1] < pref_sum[min_pref_sum_i]:
        min_pref_sum_i = i - 1

    cur_sum = pref_sum[i] - pref_sum[min_pref_sum_i]
    if max_sum < cur_sum:
        max_sum = cur_sum
        max_pref_sum_i = i

print(max_sum)
