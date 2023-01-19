# 최대 K번의 바꿔치기 연산 : 배열 A 원소 하나와 B 원소 하나 골라 바꿔치기
# 배열 A의 모든 원소의 합이 최대가 목표
# => A에서 가장 원소 골라, B에서 가장 큰 원소와 교체

import sys
n, k = map(int, sys.stdin.readline().split()) # N과 K를 입력 받기
a = list(map(int, sys.stdin.readline().split())) # 배열 A의 모든 원소를 입력받기
b = list(map(int, sys.stdin.readline().split())) # 배열 B의 모든 원소를 입력받기

a.sort()
b.sort(reverse=True)

for i in range(k):  # 두 배열의 원소를 최대 K번 비교
    # A의 원소가 B의 원소보다 작은 경우
    if a[i] < b[i]:
        # 두 원소를 교체
        a[i], b[i] = b[i], a[i]
    else: # A의 원소가 B의 원소보다 크거나 같을 때, 반복문을 탈출
        break

print(sum(a))
# 두 배열의 원소가 최대 100,000개까지 입력될 수 있음 => O(NlogN)을 보장하는 정렬 알고리즘을 사용해야 한다