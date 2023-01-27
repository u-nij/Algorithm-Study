import sys

n = sys.stdin.readline().rstrip()
market_items = list(map(int, sys.stdin.readline().split()))
m = sys.stdin.readline().rstrip()
request_items = list(map(int, sys.stdin.readline().split()))

market_items.sort()
request_items.sort()

answer = []

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        if array[mid] == target:
            print('yes', end =' ')
            return
        # 중간점 인덱스 갱신
        if array[mid] > target: # 찾으려는 값이 중간점보다 작을 때
            end = mid - 1
        else: # 찾으려는 값이 중간점보다 클 때
            start = mid + 1
    print('no', end =' ')
    return

for request_item in request_items:
    binary_search(market_items, request_item, 0, len(market_items) - 1)


# 계수 정렬로도 풀 수 있다
# 모든 원소의 번호를 포함할 수 있는 크기의 리스트를 만든 뒤
# 리스트의 인덱스에 직접 접근해 특정한 번호의 부품이 매장에 존재하는지 확인
n_ = int(input())
market_items_srt = [0] * 1000001
for i in input().split():
    market_items_sort = 1
for request_item in request_items:
    if market_items_sort[request_item] == 1:
        print('yes', end =' ')
    else:
        print('no', end =' ')

# 집합 자료형을 이용해 풀 수도 있다(특정 수가 한 번이라도 등장했는지 검사하면 되기 때문에)
# set() 함수는 집합 자료형을 초기화할 때 사용한다
# 이러한 집합 자료형은 단순히 특정한 데이터가 존재하는지 검사할 때 효과적으로 사용할 수 있다
market_items_set = set(map(int, sys.stdin.readline().split()))
for request_item in request_items:
    if market_items_set[request_item] == 1:
        print('yes', end =' ')
    else:
        print('no', end =' ')