import math

n, m, k = map(int, input().split())

def nCr(n, r):
    return math.factorial(n) / (math.factorial(n-r) * math.factorial(r))

total = nCr(n, m)
print(total)
p = 0
while k <= m:
    if n-m >= m-k:
        p += nCr(m, k) * nCr(n-m, m-k)
    else:
        continue

print(p/total)
