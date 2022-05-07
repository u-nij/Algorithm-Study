import sys
data = sys.stdin.readline().rstrip()
li = list(map(int, data))
len_li = len(li)

result = li[0]

idx = 1
while idx < len_li:
    if  li[idx] <= 1:
        result += li[idx]
    else:
        result *= li[idx]
    idx += 1

print(result)