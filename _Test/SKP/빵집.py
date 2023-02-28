# 정해진 시각, 개수만큼 빵
# 시간표와 현재 시각 구워질때, k개 판매하려면 최소 몇분 걸리는지
# 00:00(24) 0()


# 24시간 표기법
bakery_schedule = ["12:00 10"] # 1~100 길이, 빵 개수는 1~1000개
current_time = "12:00" # 현재 시각
k = 10 # 빵의 개수
result = -2

# 현재시각 XX:YY
current_hour, current_min = list(map(int, current_time.split(":")))

time = -1
for i in range(len(bakery_schedule)):
    bakery_time, num_of_bakery = bakery_schedule[i].split()
    bakery_hour, bakery_min = list(map(int, bakery_time.split(":")))
    if bakery_hour >= current_hour and bakery_min >= current_min:
        k -= int(num_of_bakery)
        if k <= 0:
            time = (bakery_hour - current_hour) * 60 + (bakery_min - current_min)
            break

# 빵이 다 팔렸을 경우
if k <= 0:
    print(time)
# 빵이 다 안팔렸을 경우
else:
    print(-1)