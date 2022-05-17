n =int(input())
j = []
for _ in range(n):
    p = int(input())
    m = list(map(int, input().split()))
    x = min(m)
    s = 0
    for i in range(p):
        if m[i] != x:
            s+=(m[i]-x)
    j.append(s)
for i in j:
    print(i)
