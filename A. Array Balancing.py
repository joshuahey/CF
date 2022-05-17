n = int(input())
e = []
for _ in range(n):
    p = int(input())
    m = list(map(int, input().split()))
    o = list(map(int, input().split()))
    s = 0
    for i in range(p-1):
        s += min(abs(m[i]- m[i+1]) + abs(o[i]- o[i+1]), abs(o[i]- m[i+1])+ abs(m[i]- o[i+1]))
    print(s)