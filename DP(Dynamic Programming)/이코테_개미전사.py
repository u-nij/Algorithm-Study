# 차례대로 식량 창고를 턴다는 가정하에,
# 1. 식량창고를 털지 않털지 결정 & 2. i번째 식량창고에 대해 털지 안 털지 결정
# i-1번째를 털 경우 -> i 털지 못함
# i-2번째를 털 경우 -> i 털지 안 털지 결정. 최대값이므로 i를 터는 경우를 생각
# a_i = max(a_i-1, a_i-2 + k_i)

import sys

n = int(sys.stdin.readline().rstrip()) # 식량창고 개수
k = list(map(int, sys.stdin.readline().split())) # 식량창고 저장된 식량 개수

d = [0] * 10
d[1] = k[0]
d[2] = max(k[0], k[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])