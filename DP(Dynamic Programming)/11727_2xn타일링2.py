# i) n-1+1일 경우, 1x2 1개
# ii) n-2+2일 경우, 2x2 2개, 혹은 2x2 1개

import sys
sys.setrecursionlimit(2000)

n = int(input())
d = [0]*1001

def dp(x) :
    if x == 1:
        return 1
    if x == 2:  # 1x2 2개, 2x1 2개, 2x2 2개
        return 3
    if d[x] != 0:
        return d[x]  # 동일한 계산을 해야 할 때, 값을 반환해 사용
    
    # Memoization; 값이 없을 때 연산해 배열을 채워줌
    d[x] = (dp(x-1) + 2 * dp(x-2)) % 10007
    return d[x]

print(dp(n))