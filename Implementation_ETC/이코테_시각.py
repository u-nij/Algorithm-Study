# 완전 탐색(Brute Forcing)
# 하루 24 * 60 * 60 = 86400 => 시간 OK
# 자바, C++로 풀 경우, m%10 == 3 || m/10 == 3인지 확인할 수 있음ㅁ

import sys

h = int(sys.stdin.readline().rstrip())

cnt = 0
for i in range(h + 1):
    for j in range(60):
        for  k in range(60):
            if '3' in str(i) + str(j) + str(k):
                cnt += 1
                
print(cnt)