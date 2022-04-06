n = int(input())
a = [0]
a[1:] = list(map(int, input().split()))
b = [1001 for _ in range(n+1)]
b[n] = 0


for i in range(n-1, 0, -1):
    if a[i] == 0:   # 진행할 수 없는 경우
        b[i] = -1
        continue

    if i + a[i] >= n:   # 오른쪽 끝으로 점프할 수 있는 경우
        b[i] = 1
        continue
    else:
        for j in range(i+1, i+a[i]+1):
            if b[j] != -1:
                b[i] = min(b[i], b[j]+1)
        if b[i] == 1001:
            b[i] = -1
        
print(b[1])

    
