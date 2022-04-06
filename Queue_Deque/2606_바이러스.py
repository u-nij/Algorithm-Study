from collections import deque
net = {}

n = int(input())
net = [[] for _ in range(1+n)]  #2차원 배열 [[], [], ... ]

com = int(input())
for i in range(com):
    a, b = map(int, input().split())
    net[a].append(b)
    net[b].append(a)

visited = [False] * (1+n)
q = deque([1])  # [1]을 deque 자료 구조에 추가
while q:
    v = q.popleft() # 맨 앞에 있는 것 pop
    for i in net[v]:    # pop한 노드에 이어진 노드들 순회
        if not visited[i]:  # 방문하지 않은 노드라면
            visited[i] = True
            q.append(i)
            
print(sum(visited)-1)   # 자기 자신을 뺌