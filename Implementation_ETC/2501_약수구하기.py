import sys

n, k = map(int, sys.stdin.readline().split())
data = []
for i in range(1, n+1):
    if n % i == 0:
        data.append(i)

if len(data) >= k:
    print(data[k-1])
else:
    print(0)