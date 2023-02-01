import sys

str = list(sys.stdin.readline())
answer = 0
init = str[0]

for s in str:
    if init != s:
        answer += 1
        init = s

if answer % 2 != 0:
    answer = answer // 2 + 1
else:
    answer = answer // 2

print(answer)

# ======================================================
# 이코테 코드

count0 = 0
count1 = 0
if str[0] == '1':
    count0 += 1
else:
    count1 += 1

for i in range(len(str)- 1):
    if str[i] != str[i+1]:
        if str[i+1] == '1':
            count0 += 1
        else:
            count1 += 1
print(min(count0, count1))