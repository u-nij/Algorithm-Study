import sys

n, m = map(int, sys.stdin.readline().split())
a, b, d = map(int, sys.stdin.readline().split())

game_map = [0] * n
for i in range(n):  # 육지 0, 바다 1
    game_map[i] = list(map(int, sys.stdin.readline().split()))

visitied = [[False] * m for _ in range(n)]

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


count = 1
turn_num = 0    # 회전 횟수

while True:
    # 왼쪽으로 회전
    d -= 1
    if d < 0:
        d = 3
    # 이동 좌표 예측
    na = a + dx[d]
    nb = b + dy[d]

    # 가보지 않은 칸이 존재하고, 육지일 경우
    if visitied[na][nb] == False and game_map[na][nb] == 0:
        a, b = na, nb   # 이동
        visitied[na][nb] = True
        count += 1
        turn_num = 0
        continue
    # 가보지 않은 칸이 없을 경우
    else:
        turn_num += 1   # -> 회전 축적
    
    # 네 방향 모두 이미 가본 칸이거나, 바다일 경우
    if turn_num >= 4:
        # 한 칸 뒤로 이동
        na = a + dx[d]
        nb = b + dy[d] 
        # 이동할 방향이 바다일 경우
        if game_map[na][nb] == 1:
            break
        else:   #바다가 아닐 경우 이동
            a, b = na, nb
        turn_num = 0

print(count)