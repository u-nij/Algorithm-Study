# 3xn
# i) n-2+2일 경우, 3가지
#  i)의 경우만 보고, D[n] = 3 * D[n-2] 라고 생각하면 안됨
# ii) n-4+4일 경우, 2가지
# iii) n-6+6일 경우, 2가지
# ...
# D[n] = 3 * D[n-2] + (2 * D[n-4] + 2 * D[n-6] + ... + 2 * D[0])

import sys
sys.setrecursionlimit(2000)

n = int(input())
d = [0]*1001

def dp(x):
    if x == 0:
        return 1
    if x == 1:
        return 0
    if x == 2:
        return 3
    if d[x] != 0:
        return d[x]

    result = 3 * dp(x-2)

    i = 3
    while i <= x:
        if i % 2 == 0:
            result += 2 * dp(x-i)
        i += 1

    d[x] = result
    return d[x]

print(dp(n))