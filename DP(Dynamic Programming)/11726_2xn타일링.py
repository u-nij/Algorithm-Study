# 길이가 n : 1~1000
# 1일 때, 1. 2일 때, 2. 3일 때, 3, ...

# i) 새롭게 1개를 추가(n-1+1)하는 경우에는, 1x2인 것 1개 추가하는 경우: 1가지
# ii) 새롭게 2개를 추가(n-2+2)하는 경우에는, 2x1인 것 2개 추가하는 경우: 1가지
# 1x2인 것 2개 추가는 i)의 경우에 포함됨
# D[n] = D[n-1] + D[n-2]
import sys
sys.setrecursionlimit(2000)

n = int(input())
d = [0]*1001

def dp(x) :
    if x == 1:
        return 1
    if x == 2:
        return 2
    if d[x] != 0:
        return d[x]  # 동일한 계산을 해야 할 때, 값을 반환해 사용
    
    # Memoization; 값이 없을 때 연산해 배열을 채워줌
    d[x] = (dp(x-1) + dp(x-2)) % 10007
    return d[x]

print(dp(n))