N, M, K = map(int, input().split())
data = list(map(int, input().split()))

data.sort()
first = data[N-1]
second = data[N-2]

# K+1마다 반복되는 수열의 형태 {f, f, f, s}
# 가장 큰 수가 더해지는 횟수
# = 수열 반복 횟수 + 나머지 횟수(first가 추가로 더해지는 횟수)
count = int(M / (K+1) * K + M % (K+1))

result = 0
result += count * first
result += (m - count) * second

print(result)