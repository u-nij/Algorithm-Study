# 1 X 1 크기 정사각형 n x n
# 길과 벽
# 길 칸 하나에 캐릭터 하나

# 캐릭터 꽃 심음
# 1. 상하좌우 방향 정함
# 1-1. 이동 불가능 할경우, 현재 위치에 꽃 심고 더 이동X
# 2. 현재 위치에 꽃 심고 *** 1번에서 정한  방향으로 이동
# 3. 더 이동하지 못할 때까지 방향 유지하고 이동

# 벽, 꽃 심어진 칸 이동 불가
# 방향 이동 불가능하면 방향 바꾸기 위해 1번 과정으로 이동

# 모든길에 꽃 심기 가능하면 1, 아니면 0

# 맵 개수 2~10
# 맵 세로가로 길이 3~10
# 벽0 길1 캐릭터2

boards = [["1111", "1121", "1001", "1111"]]
answer = []


import copy

# 바이러스 이동 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 캐릭터가 이동할 수 있을 떄까지 직진
def move(x, y, i):
    #  맵 밖이거나 벽에 부딪히거나 꽃이 있을 경우 방향 회전
    if change_direction:
        for d in range(4):
            if d % 2 != i % 2:
                move(x, y, d)
    
    # 현재 위치에 꽃 배치
    temp[x][y] = -1

    # 다음 위치
    nx = x + dx[i]
    ny = y + dy[i]
    # 맵 내에서 움직임
    if nx >= 0 and nx < len_board and ny >= 0 and ny < len_board:
        # 길 위일 경우 재귀적 수행
        if temp[nx][ny] == 1:
            move(nx, ny, i)
        else:
            x = nx - dx[i]
            y = ny - dy[i]
            change_direction = True


for board in boards:
    global temp, len_board, change_direction
    new_board = []
    len_board = len(board)
    temp = []
    x, y = 0, 0
    change_directio = False
    for i in range(len_board):
        new_board.append(list(map(int, board[i])))
        # 캐릭터 위치
        if new_board[i].count(2) != 0:
            x, y = i, new_board[i].index(2)

    possible = False # 모든 길에 꽃을 심을 수 있는지
    for j in range(4):
        # 꽃을 심을 수 있는 방법을 발견한 경우
        if possible:
            break
        # 이동
        temp = copy.deepcopy(new_board)
        move(x, y, j)

        for k in range(len_board):
            # 꽃이 심어지지 않은 길이 있을 경우
            if temp[k].count(1) == 0:
                possible = True
            else:
                possible = False
                break
    if possible:
        answer.append(1)
    else:
        answer.append(0)

print(answer)