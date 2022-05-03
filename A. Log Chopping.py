n = int(input())
for i in range(n):
    c, b, lst= 0, 0, []
    m = int(input())
    lst = list(map(int, input().split()))
    for j in lst:
        if j%2 == 0:
            c+=1
        else:
            b+=1
    if c%2 != 0:           
        print("errorgorn")
    else:
        print("maomao90")

