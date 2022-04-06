# i) n-1+1인 경우, 2가지
# ii) n-2+2인 경우, 3가지
# D[n] = D[n-1] * 2 + D[n-2] * 3
# 여기서 끝이 아니라,
# iii) n-4+4인 경우, 2가지
# D[n] = D[n-1] * 2 + D[n-2] * 3 + (D[n-3] * 2 + ... + D[0] * 2)

# 런타임 에러 => 2차원 DP
# (D[n-3] * 2 + ... + D[0] * 2)
# 앞의 숫자에 2씩 곱해주는 것이므로 

def dp_1d(x):
    if x == 0:
        return 1
    if x == 1:
        return 2
    if x == 2:
        return 7
    if d[x] != 0:
        return d[x]

    result = 3 * dp(x-2) + 2 * dp(x-1)

    i = 3
    while i <= x:
        result += (2 * dp(x-i)) % 1000000007
        i += 1

    d[x] = result % 1000000007
    return d[x]

# 0 2 7
# x x 1
# 2번쨰 행에서, 앞에 있던 것과 1번쨰 행의 3번째 전 것을 더해주고
# 1번째 행에서, D[n-1] * 2 + D[n-2] * 3
# 1번째 행 + 2번째 행 * 2
# 0 2 7 22 71
# x x 1 1 23
import sys
sys.setrecursionlimit(2000)

n = int(input())
d = list(0 for _ in range(1000001))
ds = list(0 for _ in range(1000001))
# 2번째 행을 2씩 고유한 경우의 수가 추가되는 것을 계산하는 용도로 사용

def dp(x):
    d[0] = 0
    d[1] = 2
    d[2] = 7
    ds[2] = 1
    i = 3
    while i <= x:
        ds[i] = (ds[i-1] + d[i-3]) % 1000000007
        d[i] = (3*d[i-2] + 2*d[i-1] + 2*ds[i]) % 1000000007
        i += 1

    return d[x]

print(dp(n))