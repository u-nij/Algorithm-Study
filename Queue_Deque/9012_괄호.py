import sys

n = int(sys.stdin.readline().rstrip())
ps_list = []
for _ in range(n):
    tmp = []
    is_break = False
    ps = sys.stdin.readline().rstrip()
    for p in ps:
        if p == '(':
            tmp.append(p)
        else:
            if len(tmp) == 0:
                is_break = True
                break
            else:
                popped = tmp.pop()
                if popped != '(':
                    is_break = True
                    break
    if len(tmp) != 0 or is_break:
        print('NO')
    elif len(tmp) == 0:
        print('YES')