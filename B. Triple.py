# cringe bruteforce solution O(n^2)

n = int(input())
result = []
for i in range(n):
    p = int(input())
    m = list(map(int, input().split()))
    for i in m:
        u, db = 0, []
        u = m.count(i)
        if u >= 3:
            db.append(i)
        if len(db)!=0:
            result.append(db[0])
            break
    if len(db) == 0:
         result.append(-1)
for i in result:
    print(i)

         

    