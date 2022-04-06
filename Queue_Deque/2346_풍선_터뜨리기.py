
# https://chaewonkong.github.io/posts/python-deque.html
# deque (데크; 양방향 큐)
from collections import deque

deq = deque()
N = int(input())
deq = deque(enumerate(list(map(int, input().split())), 1))

ans = []
while deq:
    idx, paper = deq.popleft()
    ans.append(idx)
    if len(deq) == 1:
        ans.append(deq.popleft()[0])
        break
    if paper > 0:
        for _ in range(paper - 1):
            deq.append(deq.popleft())
    else:
        for _ in range(-paper):
            deq.appendleft(deq.pop())

print(*ans)
