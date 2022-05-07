import sys

n = int(sys.stdin.readline())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

answer = 0
cnt = 0

for i in data:
    cnt += 1 # 그룹에 모험가 포함
    if cnt >= i:    # 그룹 결성
        answer += 1
        cnt = 0

print(answer)