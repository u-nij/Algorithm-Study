N = int(input())
A_n = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_, max_ = 1e9, -1e9

def calculrate(idx, ans, add, sub, mul, div):
    global min_, max_
    if idx == N:
        max_ = max(ans, max_)
        min_ = min(ans, min_)
        return
    else:
        if add:
            calculrate(idx + 1, ans + A_n[idx], add - 1, sub, mul, div)
        if sub:
            calculrate(idx + 1, ans - A_n[idx], add, sub - 1, mul, div)
        if mul:
            calculrate(idx + 1, ans * A_n[idx], add, sub, mul - 1, div)
        if div:
            calculrate(idx + 1, int(ans / A_n[idx]), add, sub, mul, div - 1)
            
calculrate(1, A_n[0], add, sub, mul, div)
print(max_)
print(min_)