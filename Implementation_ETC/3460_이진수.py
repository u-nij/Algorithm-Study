n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

for d in data:
    temp = []
    while d > 0:
        temp.append(d%2)
        d //= 2
    for i in range(len(temp)):
        if temp[i] == 1:
            print(i, end= ' ')