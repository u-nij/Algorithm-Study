def devideStr(p):
    if p == '':
        return ''
    
    left = 0    # (
    right = 0   # )
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        
        if left == right:
            u = p[0:i+1]
            v = p[i+1:len(p)]
            return u + ' ' + v

def isCorrect(u):
    while(u):
        idx = u.find('()')
        if idx == -1:
            return False
        else:
            u = u.replace('()', '')
    return True

def solution(p):
    if isCorrect(p):
        return p
    
    answer = ''
    
    devided = devideStr(p)
    if devided != '':
        u = devided.split(' ')[0]
        v = devided.split(' ')[1]
        
    if isCorrect(u):
        answer = u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        u = u[1:-1]
        u = u.replace('(', '-')
        u = u.replace(')', '(')
        u = u.replace('-', ')')
        answer += u

    
    return answer