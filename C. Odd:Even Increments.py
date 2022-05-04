# ugly solution but fast enough :)
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

# clean online solution :)
# for _ in range(int(input())):
#     n = int(input())
#     a = [int(i) for i in input().split()]
#     for i in range(2, n):
#         if a[i] % 2 != a[i-2] % 2:
#             print("NO")
#             break
#     else:
#         print("YES")
