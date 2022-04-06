import sys
n, m = map(int, sys.stdin.readline().split())

arr = [0] * 8
isUsed = [0] * 9   # 방문시 1
idx = 1

def func(x):   # 현재 x까지 수를 택한 상황에서 arr[x]를 정하는 함수
    global idx
    if x == m :   # 함수 종료
        for i in range(m) :
            print(arr[i], end=' ')
        print()
        return

    for i in range(idx, n+1):
        if isUsed[i] == 0 :
            arr[x] = i
            isUsed[i] = 1
            idx = i+1
            func(x+1)

            isUsed[i] = 0   # 모든 과정이 끝난 후
        
func(0) # 처음엔 아무런 수를 선택하지 않았으므로 0 호출