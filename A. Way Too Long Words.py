i, lst = int(input()), []
for i in range(0,i):
    lst.append(input())
for i in lst:
    if len(i) <= 10:
        print(i)
    else: 
        print(i[0], (len(i) - 2),i[len(i)-1], sep = "")