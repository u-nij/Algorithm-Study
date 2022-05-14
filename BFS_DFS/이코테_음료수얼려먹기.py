# 연결 노드 찾기 문제

import sys

n, m = map(int, sys.stdin.readline().split())
graph = [0] * n
for i in range(n):
    graph[i] = list(map(int, sys.stdin.readline().rstrip()))


# 그래프 형태로 모델링
# 특정 지점에서 이동 가능한 모든 경로에 대해 방문처리
# 1인 경우에 이동 불가능하게

# DFS
# 1. 특정 지점 상하좌우를 살펴본 뒤
#    주변 지점 중 값이 '0'이면서 아직 방문하지 않은 지점이 있다면 해당 지점 방문
# 2. 방문 지점에서 1번 과정을 반복하면 연결된 모든 지점을 방문할 수 있다
# 3. 모든 노드에 대해 1~2번 과정 반복, 방문하지 않은 지점의 수 카운트

# DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 # 방문 처리
        # 상하좌우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

# 모든 노드(위치)에 대해 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)