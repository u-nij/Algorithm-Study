import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(map(str, sys.stdin.readline().split())))

data.sort(key = lambda student: student[1])

for student in data:
    print(student[0], end = ' ')
# 정보가 100,000개까지 입력될 수 있으므로 최악의 경우 O(NlogN)을 보장하는 알고리즘 or O(N)을 보장하는 계수