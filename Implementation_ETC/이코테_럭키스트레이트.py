import sys

array = list(map(int, sys.stdin.readline().rstrip()))
start, end = 0, len(array)
mid = (start + end) // 2
if sum(array[:mid]) == sum(array[mid:]):
    print("LUCKY")
else:
    print("READY")