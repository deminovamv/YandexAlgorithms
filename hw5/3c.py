def read_and_num():
 x=[(int(num), index + 1) for index, num in enumerate(input().split())]
 x.sort()
 return x

n, m = map(int, input().split())
x = read_and_num()  #список количества людей в группе
y = read_and_num() #список количества компьютеров в классе
y_num = 0
answer = [0] * (n+1)
p = 0
for people, x_num in x:
   while y_num < len(y) and y[y_num][0] < people + 1:
     y_num += 1
   if y_num == len(y):
     break
   p += 1
   answer[x_num] = y[y_num][1]
   y_num += 1
print(p)
print(*answer[1:], sep='\n')