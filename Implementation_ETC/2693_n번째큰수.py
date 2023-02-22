import sys

n = int(input())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))
    data[i].sort()

for i in range(n):
    print(data[i][-3])
