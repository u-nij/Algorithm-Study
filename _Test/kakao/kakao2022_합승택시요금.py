import itertools

def solution(n, info):
    info_score = 0
    for idx in range(len(info)):
        if info[idx] != 0:
            info_score += 10-idx
    
    # 라이언의 과녁 경우의 수
    lion_lists = list(itertools.combinations_with_replacement([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0], n))
    lion_lists.sort() ## 
    answer = []
    diff_score = 0

    for lion_list in lion_lists:
        # 값 초기화
        apeach_score = info_score
        lion_score = 0
        lion_info = [0] * 11
        for score in lion_list:
            lion_info[10-score] += 1
        # 점수 계산
        for idx in range(len(lion_info)):
            if lion_info[idx] > info[idx]:           
                lion_score += 10-idx
                if info[idx] != 0:
                    apeach_score -= (10-idx)
        if apeach_score < lion_score and diff_score <= (lion_score - apeach_score):
                diff_score = lion_score - apeach_score
                answer = lion_info

    if answer == []:
        return [-1]  
    
    return answer

n = 9
info =	[0,0,1,2,0,1,1,1,1,1,1]
print(solution(n, info))