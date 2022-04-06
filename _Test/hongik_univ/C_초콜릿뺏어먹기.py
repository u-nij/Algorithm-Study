n, k = map(int, input().split())
choco = [0]
choco.extend(list(map(int, input().split())))
cnt = [0, 0]

# k < i 를 만족하는 i 고르기
# i <= N

i = k + 1
while(1):
    if i >= n+1:
        break

    if choco[i-k] < choco[i]:
        cnt[0] += choco[i] - choco[i-k]
        choco[i] = choco[i-k]
        choco.sort()
        cnt[1] += 1
    else:
        i += 1

print(cnt[0], cnt[1])