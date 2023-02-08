# 조건 만족 여부 검사
def is_enable(answer): # kind_of_frame: 기둥(0), 보(1)
    for x, y, stuff in answer:
        # 기둥일 경우
        if stuff == 0:
            # 바닥 위에 있는 경우 
            if y == 0:
                continue
            # 보의 한쪽 끝부분 위에 있는 경우
            if answer.count([x, y, 1]) == 1 or answer.count([x-1, y, 1]) == 1:
                continue
            # 다른 기둥 위에 있을 경우
            if answer.count([x, y-1, 0]) == 1:
                continue
            return False
        # 보일 경우
        else:
            # 한쪽 끝부분이 기둥 위에 있을 경우
            if answer.count([x, y-1, 0]) == 1 or answer.count([x+1, y-1, 0]) == 1:
                continue
            # 양쪽 끝부분이 다른 보와 동시에 연결되어 있을 경우
            if answer.count([x-1, y, 1]) == 1 and answer.count([x+1, y, 1]) == 1:
                continue
            return False
    return True
        
def solution(n, build_frame):
    answer = []
    
    # 첫 번째는 기둥을 설치해야 함
    while len(build_frame) > 0:
        if build_frame[0][2] == 0 and build_frame[0][3] == 1:
            break
        else:
            build_frame.pop(0)
    if len(build_frame) == 0: # 아무것도 구축하지 못한 경우
        return []
    
    # 이후의 구조물 설치
    for frame in build_frame:
        x, y, stuff, operate = frame
        # 설치의 경우
        if operate == 0:
            answer.remove([x, y, stuff])
            if not is_enable(answer):
                answer.append([x, y, stuff])
        # 삭제의 경우
        else:
            answer.append([x, y, stuff])
            if not is_enable(answer):
                answer.remove([x, y, stuff])
    
    return sorted(answer)

# 전체 명령의 개수는 1,000개 이하 => 시간 복잡도 O(N**3)으로 풀어도 5초라 넉넉
# => 설치 및 삭제 연산을 요구할 때마다, 일일이 전체 구조물을 확인하며 규칙 확인!

# 좀 더 전체적으로 생각할 것
# 자물쇠와 열쇠 문제에서처럼, 설치/제거=>되는지 확인=>안되면 원상복구