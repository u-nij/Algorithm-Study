import sys
n = int(sys.stdin.readline())
score = list(map(int, input().split()))
x, y = map(int, input().split())

x = int(n*x/100)

cnt = 0
for i in range(n):
    if score[i] >= y:
        cnt += 1

print(x, cnt)