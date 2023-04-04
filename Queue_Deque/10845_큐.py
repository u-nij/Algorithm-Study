import sys
from collections import deque

queue = deque()
n = int(sys.stdin.readline())
for i in range(n):
    inst = sys.stdin.readline().rstrip()
     
    if 'push' in inst:
        queue.append(inst.split()[1])
    elif inst == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            popped = queue.popleft()
            print(popped)
    elif inst == 'size':
        print(len(queue))
    elif inst == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif inst == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif inst == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])
