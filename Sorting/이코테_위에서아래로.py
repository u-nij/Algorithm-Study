import sys

n = int(sys.stdin.readline())
array = []
for i in range(n):
    array.append(int(sys.stdin.readline()))

array.sort(reverse=True)

for i in array:
    print(i, end = ' ')
# 모든 수는 1~100,000이므로 어떠한 정렬 알고리즘을 사용해도 해결 가능