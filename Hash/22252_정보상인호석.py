q = int(input())
dict = {}
ans = 0

for i in range(q):
    a = list(input().split())
    op = a[0]
    name = a[1]
    num = int(a[2])  # 개수 k or b
    del a[:3]

    if op == '1':
        a = list(map(int, a))   # to int
        a = a[:num]
        # create or update
        if name in dict:
            tmp = dict.get(name)
            tmp.extend(a)
            del dict[name]
            tmp.sort(reverse=True)
            dict[name] = tmp
        else:
            a.sort(reverse=True)
            dict[name] = a
    elif op == '2':
        if name in dict:
            tmp = dict.get(name)
            del dict[name]
            if len(tmp) > num:
                ans += sum(tmp[:num])
                dict[name] = tmp[num:]
            else:
                ans += sum(tmp)

print(ans)