import sys

stack = []
n = int(sys.stdin.readline())
for i in range(n):
    inst = sys.stdin.readline().rstrip()
     
    if 'push' in inst:
        stack.append(inst.split()[1])
    elif inst == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            popped = stack.pop()
            print(popped)
    elif inst == 'size':
        print(len(stack))
    elif inst == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif inst == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
