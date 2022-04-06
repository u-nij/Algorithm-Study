import sys
sys.setrecursionlimit(2000)
input = sys.stdin.readline

n = int(input())
score = [0] * 301
for i in range(1, n+1):
    score[i] = int(input())

d = [0] * 301
d[1] = score[1]
d[2] = score[1] + score[2]

def dp(x):
    if x == 0:
        return 0
    if d[x] != 0:
        return d[x]
    
    # (n-2, n) OR (n-3, n-1, n)
    d[x] = max(dp(x-2)+score[x], dp(x-3)+score[x-1]+score[x])
    return d[x]

if n <= 2:
    print(d[n])
else:
    print(dp(n))