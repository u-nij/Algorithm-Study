import math

def solution(fees, records):
    answer = []
    
    my_records = {}
    my_answer = {}
    for record in records:
        record = record.split(" ")
        if record[2] == "IN":
            my_records[record[1]] = record[0]
        else: # "OUT"
            # 주차 시간 계산
            InTime = my_records[record[1]].split(":")
            InMin = int(InTime[0])*60 + int(InTime[1])
            OutTime = record[0].split(":")
            OutMin = int(OutTime[0])*60 + int(OutTime[1])
            parkingTime = OutMin - InMin
            # 주차 시간 저장
            if record[1] in my_answer:
                my_answer[record[1]] += parkingTime
            else:
                my_answer[record[1]] = parkingTime
            del my_records[record[1]]

    # 출차하지 않은 차량
    if my_records:
        for record in my_records.keys():
            InTime = my_records[record].split(":")
            InMin = int(InTime[0])*60 + int(InTime[1])
            OutMin = 23*60 + 59
            parkingTime = OutMin - InMin
            # 주차 시간 저장
            if record in my_answer:
                my_answer[record] += parkingTime
            else:
                my_answer[record] = parkingTime

    # 요금 계산
    for car in my_answer.keys():
        fee = 0
        parkingTime = my_answer[car]
        if parkingTime > fees[0]:
            fee = fees[1] + math.ceil((parkingTime-fees[0])/fees[2]) * fees[3]
        else:
            fee = fees[1]
        my_answer[car] = fee

    # 차량 번호 오름순 정렬
    my_answer = sorted(my_answer.items())
    print(my_answer)
    for a in my_answer:
        answer.append(a[1])
        
    return answer