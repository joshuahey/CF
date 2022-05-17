n = int(input())
for _ in range(n):
    p = input()
    s, s2= 0, 0
    for i in range(0,3):
        s+=int(p[i])
    for i in range(3,6):
        s2+=int(p[i])
    if s == s2:
        print("YES")
    else:
        print("NO")
    

    
        