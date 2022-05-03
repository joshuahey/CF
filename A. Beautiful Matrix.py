matrix  = []
for i in range(5):
    lst = []
    lst = list(map(int, input().split()))
    matrix.append(lst)
for i in range(5):
    for j in range(5):
        if matrix[i][j] == 1:
            print(abs(i-2)+ abs(j-2))
