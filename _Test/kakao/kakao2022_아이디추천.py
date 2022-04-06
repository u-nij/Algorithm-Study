def solution(id_list, report, k):
    len_id = len(id_list)
    answer = [0] * len_id
    report_list = [[0] * len_id for _ in range(len_id)] 
    reported = [0] * len_id
    
    report = list(set(report))
    for r in report:
        reported_idx = id_list.index(r.split(" ")[1])
        report_list[id_list.index(r.split(" ")[0])][reported_idx] = 1
        reported[reported_idx] += 1
    
    for j in range(len(reported)):
        if reported[j] >= k:
            for i in range(len_id):
                if report_list[i][j] == 1:
                    answer[i] += 1
        
    return answer