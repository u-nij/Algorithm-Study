# union-find
import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n, m = map(int, input().split())
parent = [i for i in range(n+1)]

def find(a):
    if a == parent[a]:
        return a

    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return
    elif a < b:
        parent[b] = a
    else:
        parent[a] = b

for i in range(0, m):
    op, a, b = map(int, input().split())
    if op == 0 :
        union(a, b)
    else:
        if find(a) == find(b):  # parent same
            print('YES')
        else:
            print('NO')