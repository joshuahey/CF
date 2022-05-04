# trying to shorten the code but slower
n = int(input())
for i in range(n):
    l = int(input())
    m = list(map(int, input().split()))
    p, g= False, False
    for i in range(0, l-2):
        if (m[i] %2 == m[i+2] %2) :
            p = True
        else:
            p = False
            break
    if p == True or (l == 0 or l == 1 or l == 2):
        print("YES")
    else:
        print("NO")

# ugly solution but fastest in online python submissions
n = int(input())
for i in range(n):
    l = int(input())
    m = list(map(int, input().split()))
    p, g= False, False
    for i in range(0, l-2, 2):
        if (m[i] %2 == 0 and m[i +2] %2 == 0) or (m[i] %2 != 0 and m[i +2] %2 != 0) :
            p = True
        else:
            p = False
            break
    if l == 3:
        g = True
    for i in range(1, l-2, 2):
        if (m[i] %2 == 0 and m[i +2] %2 == 0) or (m[i] %2 != 0 and m[i +2] %2 != 0):
            g =True
        else:
            g =False
            break
    if l == 0 or l == 1 or l == 2:
        print("YES")
    else:
        if p == g == True:
            print("YES")
        else:
            print("NO")
