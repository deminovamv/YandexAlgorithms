n = int(input())
n_list = [0] * n
topics = [''] * n
for i in range(n):
    k = int(input())
    if k == 0:
        n_list[i] = i
        topics[i] = input()
        input()
    else:
        n_list[i] = n_list[k-1]
        input()
n_dict = {}
for rep in n_list:
    n_dict[rep] = n_dict.get(rep, 0) + 1
ans = []
for topic in n_dict:
    ans.append((-n_dict[topic],topic))
print(topics[min(ans)[1]])