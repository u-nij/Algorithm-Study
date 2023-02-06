import sys

# 보드
n = int(sys.stdin.readline().rstrip())
# 사과
k = int(sys.stdin.readline().rstrip())
apples = [[0] * (n+1) for _ in range(n+1)]
for i in range(k):
    y, x = map(int, sys.stdin.readline().split())
    apples[y][x] = 1
# 방향 변환 횟수
l = int(sys.stdin.readline().rstrip())
moving = [0] * l
for i in range(l):
    second, direction = map(str, sys.stdin.readline().split())
    moving[i] = [int(second), direction]

# 초기화
direction = 0
snake = []
snake.append((1, 1))
x, y = 1, 1

# 이동 방향
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
move_types = ['R', 'D', 'L', 'U']


def get_direction(now, next):
    if next == 'L':
        return (now - 1) % 4
    else:
        return (now + 1) % 4


sec = 0 # 게임 진행 시간
while 1:
    # 이동 및 진행 시간 증가
    sec += 1
    x, y = x + dx[direction], y + dy[direction]
    if x < 1 or x > n or y < 1 or y > n or snake.count((x, y)) != 0: # 벽이나 자기 자신의 몸과 부딪히면 게임 종료
        break
    snake.append((x, y))
    # 이동한 칸에 사과가 있을 경우 사과 제거
    if apples[y][x] == 1:
        apples[y][x] = 0
    # 사과가 없을 경우 꼬리 비움
    else:
        snake.pop(0)
    # 방향 전환이 있을 경우
    if len(moving) > 0 and moving[0][0] == sec:
        direction = get_direction(direction, moving[0][1])
        moving.pop(0)

print(sec)
