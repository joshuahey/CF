n =int(input())
for i in range(n):
    k = int(input())
    m = list(map(int, input().split()))
    c, j= 0, 0
    while j < k-1:
        if m[j] >= m[j+1] or m[j]==0 and k>0: 
            c = -1
            break
        if m[j] >= m[j+1]:
            m[j] = m[j]//2
            c+=1
            j = 0
        else:
            j+=1
    print(c)
