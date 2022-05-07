n, k = map(int, input().split())

count = 0

# while n != 1:
#   if n % k == 0:
#     n //= k
#   else:
#     n -= 1
#   count += 1

# N이 100억 이상의 큰 수일때
while True:
  # tmp = N이 K로 나누어지는 수
  tmp = (n // k) * k   
  count += n - tmp
  
  n = tmp  
  if n < k:
    break

  n //= k
  count += 1

count += n-1
print(count)


# N이 아무리 큰 수여도, K로 계속 나눈다면 빠르게 줄일 수 있다.
# => K로 나누는 것이 1을 빼는 것보다 빠르게 N을 줄일 수 있다.