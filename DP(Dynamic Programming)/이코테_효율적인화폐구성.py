import sys

n, m = map(int, sys.stdin.readline().split())
coin = []
d = [10001] * (m+1) # i원을 만들기 위한 최소한의 화폐 개수
for i in range(n):
    coin.append(int(input()))

# 불가능할 경우: 코인으로 나눠지지 않을 경우
# a_i-k를 만들 수 있는 경우: a_i = min(a_i, a_i-k + 1) (a=최소한의 화폐 개수, k=화폐 단위)

d[0] = 0
for i in range(n):
    for j in range(coin[i], m+1):
        if d[j-coin[i]] != 10001:
            d[j] = min(d[j], d[j-coin[i]] + 1)


print(d[m] if d[m] != 10001 else -1)