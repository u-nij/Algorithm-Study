import sys
n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
ans = 0
arr = [0] * n
isUsed = [0] * n

def func(x):
    global ans
    if x == n:
        j = 0
        sum = 0
        while j <= n:
            if j == n-1:
                break
            sum += abs(arr[j]-arr[j+1])
            j += 1
        ans = max(ans, sum)
        return
    
    for i in range(n):
        if isUsed[i] == 0:
            arr[x] = a[i]
            isUsed[i] = 1
            func(x+1)
            isUsed[i] = 0

func(0)
print(ans)