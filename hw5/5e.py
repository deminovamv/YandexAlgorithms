s = int(input())
a_array = [int(num) for num in input().split()]
b_array = [int(num) for num in input().split()]
c_dict = {}
for index, elem in enumerate(map(int, input().split())):
    if index != 0:
        if elem not in c_dict:
          c_dict[elem] = index -1

def solution():
    for i in range(1, a_array[0]+1):
        for j in range(1, b_array[0]+1):
            num_to_find = s - a_array[i] - b_array[j]
            print(num_to_find)
            if num_to_find in c_dict:
                return f"{i-1} {j-1} {c_dict[num_to_find]}"
    return "-1"
print(c_dict)
print(solution())