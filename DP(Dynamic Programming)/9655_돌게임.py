import sys
sys.setrecursionlimit(2000)

n = int(input())


def dp(x):
    if x == 0:
        return 'SK'
    if x == 1:
        return 'CY'
    if x == 2:
        return 'SK'
    if x == 3:
        return 'CY'
    
    if x>=4:
        dp(x-3)

ans = dp(n)
print(ans)