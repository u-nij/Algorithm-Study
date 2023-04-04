import sys
n = int(sys.stdin.readline())
ary = list(map(int, sys.stdin.readline().split()))
ary.sort()
print(ary[0] * ary[-1])