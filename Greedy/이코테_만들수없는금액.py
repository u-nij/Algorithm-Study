import sys

n = int(sys.stdin.readline().rstrip())
data = list(map(int, sys.stdin.readline().split()))
data.sort()

target = 1 # 만들 수 있는 금액

for x in data: # 화폐가 작은 동전부터 
    # 만들 수 없는 금액을 찾았을 때 종료
    if target < x:
        break
    target += x

print(target)
# 1 -> 2 -> 4 -> 7 (6까지 만들 수 있다는 말이 된다)