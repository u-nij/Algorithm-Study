# 시간이 적게 걸리는 음식부터 확인하는 탐욕적 접근 방법으로 해결
# 음식을 시간을 기준으로 정렬한 뒤, 시간이 적게 걸리는 음식부터 제거해 나가기
# => 우선순위 큐를 이용

# 1. 모든 음식을 우선순위 큐(최소 힙)에 튜플 형태로 삽입한다. (음식 시간, 음식 번호)
# 2. 첫 단계에서는 가장 적게 걸리는 3번 음식을 뺀다. 음식이 3개 남아있으므로 3(남은 음식)*4(3번 음식을 다 먹는 시간)=12를 k에서 뺀다
# 3. 이번 단계에서는 2번 음식을 뺀다. 전체 음식이 2개 남아있으므로 2(남은 음식)*2(2번 음식을 다 먹는 시간)=4를 뺴야하지만, 남은 시간이 3초이므로 빼지 않는다
#  => 다음으로 먹어야 할 음식의 번호를 찾아 출력한다.

import sys, heapq

food_times = list(map(int, sys.stdin.readline().split())) # 각 음식을 모두 먹는데 필요한 시간
k = int(sys.stdin.readline().rstrip()) # 방송이 중단된 시간

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 뺴야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 삽입
        heapq.heappush(q, (food_times[i], i+1))

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # 먹기 위해 사용한 시간 + (현재 음식 시간 - 이전 음식 시간) * 현재 음식 개수 vs. k
    # 가장 적게 걸리는 음식을 다 먹을 수 있는 경우 
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0] # 현재 음식 시간
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식이므로
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]

print(solution(food_times, k))