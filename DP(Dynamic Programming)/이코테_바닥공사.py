# i-1까지 이미 채워져 있으면 2*1 덮개: 1개의 경우
# i-2까지 이미 채워져 있으면 1*2 2개 혹은 2*2 1개로: 2개의 경우
# 덮개의 형태가 최대 2*2 크기의 직사각형 형태이기 때문에, i-3 이하의 위치에 대한 최적의 해는 고려할 필요 없다
# a_i = a_i-1 + a_i-2 * 2

import sys

n = int(input())
d = [0] * 1001
d[1] = 1
d[2] = 2

for i in range(3, n+1):
    d[i] = (d[i-1] + d[i-2] * 2) / 796796

print(d[n])