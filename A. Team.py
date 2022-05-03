n, c = int(input()), 0
for i in range(0,n):
    x = list(map(int, input().split()))
    if sum(x) >=2 :
        c +=1
print(c)
