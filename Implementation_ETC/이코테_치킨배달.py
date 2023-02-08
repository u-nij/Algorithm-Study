import sys
from itertools import combinations


n, m = map(int, sys.stdin.readline().split())
# city = [] # 전체를 저장하는 대신, 집 저장
chicken = []
house = []

for y in range(n):
    c = list(map(int, sys.stdin.readline().split()))
    for x in range(n):
        if c[x] == 1:
            house.append([x, y])
        if c[x] == 2:
            chicken.append([x, y])

# m개의 치킨집 뽑는 조합
m_of_chicken = list(combinations(chicken, m))

# m개의 무작위 치킨집 중 해당 집의 치킨거리
# def get_distance(house_x, house_y, chicken_list):
#     min = int(1e9)
#     for c in m_of_chicken:
#         chicken_x, chicken_y = c
#         dis = abs(house_x - chicken_x) + abs(house_y - chicken_y)
#         if dis < min:
#             min = dis
#     return min

# min = int(1e9)
# for chicken_list in m_of_chicken:
#     tmp = 0
#     for i in range(n):
#         for j in range(n):
#             if city[i][j] == 1:
#                 tmp += get_distance(j, i, chicken_list)
#     if min > tmp:
#         min = tmp


# 모든 집에 대해 m개의 치킨 거리의 합을 계산
def sum_of_chicken_distance(candidate):
    result = 0
    for hx, hy in house: # 각 집에 대해
        temp = int(1e9)
        for cx, cy in candidate: # 가장 가까운 치킨집 거리 구하기
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        result += temp
    return result

# 치킨 거리의 합의 최소를 찾아 출력
result = int(1e9)
for candidate in m_of_chicken:
    result = min(result, sum_of_chicken_distance(candidate))

print(result)


# 원래 방식
# 도시에서 일일히 집을 찾은 후에
# 조합에서 뽑혀나온 m개의 치킨집에 대해
# 하나의 집에서부터 치킨 거리를 더하면서 반복
# O(n*n*조합개수*m)

# 개선
# 일일히 찾지 않고, 집인 것을 따로 빼옴
# O(집*조합개수*m)