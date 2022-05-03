m ,n = map(int, input().split())
if (m == 0 or n == 0 ) or (m == 1 and n ==1):
    print(0)
else:
    print((m*n)//2)