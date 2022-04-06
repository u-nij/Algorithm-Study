import sys
n, k = map(int, sys.stdin.readline().split())
kit = list(map(int, sys.stdin.readline().split()))
w = 0

cnt = 0
isUsed = [0] * n

def func(x):
    global cnt, w
    if x == n:
        cnt += 1
        return
    
    for i in range(n):
        if isUsed[i] == 0:
            if w+kit[i]-k >= 0:
                w = w + (kit[i]-k)
                isUsed[i] = 1
                func(x+1)
                w = w - (kit[i]-k)
                isUsed[i] = 0

func(0)
print(cnt)