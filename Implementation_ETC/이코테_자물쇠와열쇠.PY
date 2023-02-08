# 시계방향으로 90도 회전
def rotate_a_matrix_by_90_degree(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - 1 - i] = a[i][j]
    return result

# 자물쇠 중간부분 체크
def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    # 초기화
    len_key = len(key)
    len_lock = len(lock)
    # 자물쇠 크기 3배로
    # 정말 세밀하게 표현할 필요 없음! len_lock + len_key * 2 - 2 이런식으로 안해도 됨..
    new_lock = [[0] * (len_lock * 3) for _ in range(len_lock * 3)]
    for i in range(len_lock):
        for j in range(len_lock):
            new_lock[i+len_lock][j+len_lock] = lock[i][j]
    
    # 자물쇠 홈과 열쇠의 홈 비교
    # 처음 key[0][0]의 위치가 new_lock[len_lock-len_key+1][len_lock-len_key+1]
    # 맨 끝은 new_lock[2*len_lock][2*len_lock]
    # new_lock[len_lock:len_lock*2][len_lock:len_lock*2]가 모두 1이면 TRUE 리턴
    
    for _ in range(4): # 4가지 방향에 대해 확인
        key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
        for i in range(len_lock-len_key+1, 2*len_lock):
            for j in range(len_lock-len_key+1, 2*len_lock):
                # 자물쇠 홈 맞추기
                for k in range(len_key):
                    for m in range(len_key):
                        new_lock[k+i][m+j] += key[k][m]
                # 자물쇠 중간 부분이 모두 1인지 확인
                if check(new_lock) == True:
                    return True
                # 자물쇠 빼기
                for k in range(len_key):
                    for m in range(len_key):
                        new_lock[k+i][m+j] -= key[k][m]
    
    return False


# deepcopy를 이용할 필요 X
# 맞추고 => 확인하고 => 값 되돌리기 