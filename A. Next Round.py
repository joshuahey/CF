n, k  = map(int, input().split())
lst = list(map(int, input().split()))
i, c= 0, 0
temp = lst[k-1]
for i in range(0,len(lst)):
    if lst[i]>=temp and lst[i]>0 :
        c+=1
print(c)


# logn solution- do last occurance binary search 
        
