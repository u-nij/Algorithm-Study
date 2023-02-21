# 모든 간선(거리)의 비용이 동일할 때는, 너비 우선 탐색을 이용하여 최단 거리를 찾을 수 있다
# 노드의 개수 N은 최대 300,000개이고 간선의 개수 M은 최대 1,000,000개
# 너비 우선 탐색을 이용해 시간 복잡도 O(N+M)으로 동작하는 소스 코드를 작성해 시간 초과 없이 해결 가능하다

# 특정 도시 X를 시작점으로 BFS를 수행하여 모든 도시까지의 최단 거리를 계산한 후,
# 각 최단 거리를 하나씩 확인하며 그 값이 K인 경우에 해당 도시의 번호를 출력하면 된다.

import sys
from collections import deque

n, m, k, x = map(int, sys.stdin.readline().split())
city = [[] for _ in range(n+1)]

# 도로 정보
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    city[a].append(b)

# x로부터 모든 도시까지 가는 최단 거리 초기화
distance = [-1] * (n+1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# BFS 수행
q = deque([x])
while q:
    now = q.popleft()
    # 현재 도시에서 이동할 수 있는 모든 도시 확인
    for next in city[now]:
        # 아직 방문하지 않은 도시라면
        if distance[next] == -1:
            # 최단 거리 갱신
            distance[next] = distance[now] + 1
            q.append(next)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True

if check == False:
    print(-1)
