import sys

n, k = map(int, sys.stdin.readline().split())
data = list(map(int, sys.stdin.readline().split()))
tap = [0] * n

# 빈 tab이 있을 경우 꽂는다
# 빈 tab이 없을 경우 기존 것을 뽑고 꽂는다
# 뽑는 기준: 안 쓰는 것, 더 나중에 사용되는 것

answer = 0
for i in range(k):
    item = data[i]
    # 이미 꽂혀있을 경우
    if item in tap:
        continue
    # 빈 tab이 있을 경우
    if tap.count(0) > 0:
        tap[tap.index(0)] = item
        continue

    # tab에 있는 것 중 뽑을 것 고르기
    temp = 0
    pull_idx = 0
    for j in range(n):
        # 후보가 더이상 사용되지 않을 경우
        if tap[j] not in data[i:]:
            pull_idx = j
            break
        # 이후에 사용될 때, 가장 나중에 사용되는거 선택
        elif data.index(tap[j]) > temp:
            temp = data.index(tap[j])
            pull_idx = j
    # 뽑은 후 새로운 것 꽂기
    answer += 1
    tap[pull_idx] = item

print(answer)