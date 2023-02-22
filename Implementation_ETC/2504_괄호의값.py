import sys

string = str(sys.stdin.readline().strip())
stack = []

tmp = 1 # 닫힌 괄호일 떄 answer에 더해줌. 이전 괄호에 따라 2 혹은 3을 나누기해줌.
answer = 0
is_calculate = False    # 닫힌 괄호일 떄 중복 계산을 피하기 위해 사용
                        # 사용하지 않으려면 for i in range(len(string))으로 변경

for str in string:
    # (, [가 나오면 스택 쌓기
    if str == '(':
        is_calculate = False
        stack.append(str)
        tmp *= 2
    elif str == '[':
        is_calculate = False
        stack.append(str)
        tmp *= 3
    # ), ]가 나오면 스택에서 꺼내 계산할 값 저장
    else:
        if str == ')':
            # 잘못된 문자열일 경우
            if not stack or stack[-1] != '(': # 스택이 비었을 경우도 체크할 것
                answer = 0
                break
            # 맨 마지막의 열린 괄호와 짝이 맞을 경우, answer 업데이트
            if stack[-1] == '(' and not is_calculate:
                is_calculate = True
                answer += tmp
            # 열린 괄호 제거해주며 tmp 되돌리기
            tmp //= 2
            stack.pop()
        else:
            if not stack or stack[-1] != '[':
                answer = 0
                break
            if stack[-1] == '[' and not is_calculate:
                is_calculate = True
                answer += tmp
            tmp //= 3
            stack.pop()

if stack:
    print(0)
else:
    print(answer)


# stack[-1] 등을 사용할 때 스택이 비었을 때 런타임 에러가 발생할 수 있다
# 스택이 비었을 때를 검사해야 한다

# 순서대로 생각하는 방법: 곱해준만큼 나눠주기