# 두 개의 자연수에 대한 최대공약수(GCD) 계산
# 유클리드 호제법 :
# 두 자연수 A,B에 대하여(A>B) A를 B로 나눈 나머지를 R
# A와 B의 최대공약수 = B와 R의 최대공약수

#  A     B
# 192   162
# 192    30
#  30    12
#  12     6

def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)

print(gcd(192, 162))
# 동작 과정상, 꼭 A > B일 필요가 없어진다.