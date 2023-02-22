import sys, math

a, b = map(int, sys.stdin.readline().split())

print(math.gcd(a, b)) # 최대 공배수
print(math.lcm(a, b)) # 최소 공배수