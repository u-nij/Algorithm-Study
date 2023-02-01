# 한 도시에서 다른 도시까지의 최단 거리 => 다익스트라
# 범위가 30,000과 200,000으로 충분히 크기 때문에 => 우선순위 큐 이용

import sys, heapq
input = sys.stdin.readline()
INF = int(1e9)

n, m, c = map(int, sys.stdin.readline().split()) # 도시 개수, 통로 개수, 메세지 출발 도시

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph = [[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보 입력받기
for _ in range(m):
    x, y, z = map(int, sys.stdin.readline().split()) # a번 노드에서 b번 노드로 가는 비용이 c
    graph[x].append(y, z) #[인접 노드, 비용]

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q: # 큐가 비어있지 않다면
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 수행
dijkstra(c)

# 도달할 수 있는 노드의 개수
count = 0
# 그 중 가장 멀리 있는 노드와의 최단 거리
max_distance = 0

for d in distance:
    # 도달할 수 있는 노드인 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)

print(count - 1, max_distance) # 시작노드는 제외해야 하므로 count - 1
