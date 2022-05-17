n =int(input())
p = []
for _ in range(n):
    a,b = input().split()
    q,l= [], []
    s =0
    for i in range(int(a)):
        t= 0
        m = list(input())
        for j in m:
            t +=(ord(j)-96)
        q.append(t)
    print(q)
    if len(q) == 2:
        s = abs(q[0] - q[1])
    else:
        for i in range(len(q)):
            for j in range(i, len(q)):
                if q[i]!=q[j]:
                    l.append(abs((q[i]- q[j])))
        print(l)
        s = min(l)
    p.append(s)       
for i in p:
    print(i)