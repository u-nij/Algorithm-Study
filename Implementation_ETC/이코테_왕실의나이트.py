import sys

n = sys.stdin.readline().rstrip()
str_x = ['0', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x = str_x.index(n[0])
y = int(n[1])

d_xy = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, 1)]

cnt = 0
for d in d_xy:
    nx = x + d[1]   # row
    ny = y + d[0]   # column
    if nx > 0 and ny > 0 and nx < 9 and ny < 9:
        cnt += 1

print(cnt)