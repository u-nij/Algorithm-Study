# BFS는 시작 지점에서 가까운 노드부터 차례대로 그래프의 모든 노드를 탐색
# 상하좌우로 연결된 모든 노드로의 거리가 1로 동일
# => (1, 1) 지점에서 BFS를 수행해 모든 노드의 최단 거리 값을 기록하면 해결할 수 있다


import sys

n, m = map(int, sys.stdin.readline().split())
graph = [0] * n
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().rstrip()))

# 이동할 네가지 방향 정의 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
from collections import deque

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    # 큐가 빌 때까지 반복하기
    while queue:
        x, y = queue.popleft()  # 현재 위치
        # 현재 위치에서 상하좌우 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우(값이 1인 노드)에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]

print(bfs(0, 0))

