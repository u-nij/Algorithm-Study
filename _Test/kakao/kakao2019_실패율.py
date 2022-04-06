def solution(N, stages):
    answer = []
    cnt = [0]
    fail = []
    for i in range(1, N+1):
        cnt.append(stages.count(i))

    playerCnt = len(stages)
    for i in range(1, len(cnt)):
        playerCnt -= cnt[i-1]
        if cnt[i] != 0:
            fail.append([i, cnt[i]/playerCnt])
        else:
            fail.append([i, 0])

    sortFail = sorted(fail, key=lambda x : (-x[1],x[0]))
    for i in sortFail:
        answer.append(i[0])

    return answer