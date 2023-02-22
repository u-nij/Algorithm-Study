import sys

n, m = map(int, sys.stdin.readline().split())
lab = []
temp = [[0] * m for _ in range(n)] # 벽 설치 후
for _ in range(n):
    lab.append(list(map(int, sys.stdin.readline().split())))

result = 0

# 바이러스 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# DFS 이용해 바이러스 확산
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny)

# 안전 영역 크기 계산
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

# DFS 이용해 울타리 설치하면서, 안전 영역 크기 계산
def dfs(count):
    global result
    # 울타리 3개 설치된 경우
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = lab[i][j]
        # 바이러스 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i, j)
        # 안전 영역 최대값 계산
        result = max(result, get_score())
        return
    
    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                count += 1
                # 재귀적
                dfs(count)
                # 울타리 해체
                lab[i][j] = 0
                count -= 1

dfs(0)
print(result)