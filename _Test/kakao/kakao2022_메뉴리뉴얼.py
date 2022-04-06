import math

def isPrimeNumber(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    rev_base = ''
    while n > 0: # k진수로 변환
        n, mod = divmod(n, k)
        rev_base += str(mod)
    n = rev_base[::-1]
    
    numList = str(n).split('0')
    for num in numList:
        if num != '':
            num = int(num)
            if num != 1 and isPrimeNumber(num):
                answer += 1
    
    return answer