import sys

h, w = map(int, sys.stdin.readline().split())
block = list(map(int, sys.stdin.readline().split()))

water = 0 # 고인 빗물의 양

for i in range(1, w-1):
    # 좌우 블록 높이의 최대값
    left = max(block[:i])
    right = max(block[i+1:])

    m = min(left, right)
    # 작은 값이 블록보다 크다면, 차이만큼 빗물이 고일 수 있다
    if m > block[i]:
        water += m - block[i]

print(water)