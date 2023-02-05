import sys, math

n, m = map(int, sys.stdin.readline().split()) # 볼링공 개수, 공의 최대 무게
k = list(map(int, sys.stdin.readline().split())) # 볼링공의 무게

# 인덱스=공의 무게, 값=해당 무게인 공의 개수
weight = [0] * (m+1)
for i in k:
    weight[i] += 1

answer = 0
for i in range(1, m+1):
    answer += weight[i] * sum(weight[i+1:])

print(answer)