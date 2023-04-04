import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
ary = deque([i+1 for i in range(n)])
answer = []

while(len(ary)):
    ary.rotate(-k+1)
    popped = ary.popleft()
    answer.append(popped)

answer = list(answer)
print("<", ", ".join(map(str, answer)), ">", sep="")