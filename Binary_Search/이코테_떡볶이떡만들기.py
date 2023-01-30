# 전형적인 이진 탐색 문제이자, 파라메트릭 서치 유형
# 파라메트릭 서치: 최적화 문제를 결정 문제로 바꾸어 해결. '원하는 조건을 만족하는 가장 알맞은 값을 찾는 문제'에 주로 사용
# ex. 범위 내에서 조건을 만족하는 가장 큰 값을 찾으라는 최적화 문제 => 이진 탐색으로 결정 문제를 해결하며 범위를 좁혀갈수 있다
# 반복문을 이용하면 더 간결하게 풀 수 있다.

# 절단기의 높이가 0~10억인 정수 => 이진 탐색, 최대 대략 31번
# 떡의 개수가 최대 100만 개 => 최대 3000만 번의 연산

import sys

n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(array)

height = 0
while start <= end:
    mid = (start + end) // 2
    total = sum(array) - mid * n # 잘랐을 때 떡의 양
    if total >= m: # 떡의 양이 충분한 경우 덜 자르기
        height = mid # 최대값을 찾는 것이 정답 = 최대한 덜 잘랐을 때가 정답
        start = mid + 1
    else:
        end = mid - 1

print(height)