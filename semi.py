def check(n):
    l = []
    for i in n:
        if not i in l:
            l.append(i)
    return l,len(l)

n,kn = int(input()), int(input())
m = list(map(int, input().split()))
k = []
for i in range(kn):
    l = list(map(int, input().split()))
    k.append(l)
for i in k:
    m[i[0]] = i[1]
    res = check(m)
    print(res[1],end=' ')