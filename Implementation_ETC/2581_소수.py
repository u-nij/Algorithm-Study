m = int(input())
n = int(input())

data = []

for i in range(m, n+1):
    for j in range(2, i+1):
        if i == j:
            data.append(i)
        if i % j == 0:
            break

if len(data) > 0:
    print(sum(data))
    print(data[0])
else:
    print(-1)