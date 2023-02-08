def solution(s):
    answer = len(s)

    zip_unit = len(s) // 2 # 압축 단위, 최대부터 시작
    while zip_unit >= 1:
        # 초기화
        zip_str = '' # 압축된 문자열
        tmp_str = s[0:zip_unit]
        count = 1
        # 다음 문자열이 압축된 문자열과 같은지 비교
        for i in range(zip_unit, len(s)+1, zip_unit):
            now = s[i:i+zip_unit]
            # 이전 문자열과 같을 경우 카운트 증가
            if now == tmp_str:
                count += 1
            # 이전 문자열과 다를 경우
            else:
                if count > 1:
                    tmp_str = str(count) + tmp_str
                zip_str = zip_str + tmp_str
                # 초기화
                count = 1
                tmp_str = now
            # 다음에 슬라이싱할 문자열이 압축 단위보다 짧을 경우 종료
            if i+zip_unit > len(s):
                zip_str = zip_str + s[i:] # 남은 문자열 합침
                break
        if answer > len(zip_str):
            answer = len(zip_str)
        zip_unit = zip_unit - 1
    
    return answer