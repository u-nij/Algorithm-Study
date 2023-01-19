import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(map(str, sys.stdin.readline().split())))

data.sort(key = lambda student: student[1])

for student in data:
    print(student[0], end = ' ')