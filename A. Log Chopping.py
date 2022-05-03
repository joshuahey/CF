# n = int(input())
# for i in range(n):
#     c, b, lst= 0, 0, []
#     m = int(input())
#     lst = list(map(int, input().split()))
#     for j in lst:
#         if j%2 == 0:
#             c+=1
#         else:
#             b+=1
#     if c%2 != 0:           
#         print("errorgorn")
#     else:
#         print("maomao90")
db= {}
def solution(streamerInformation, commands):
    if commands == "StreamerOnline":
        db.update({streamerInformation[0] : [streamerInformation[1], streamerInformation[2]]})
    elif commands == "UpdateViews":
        for key in db.keys():
            if streamerInformation[0] == key:
                db[streamerInformation[0]][0] = streamerInformation[1] 
    elif commands == "UpdateCategory":
        for key in db.keys():
            if streamerInformation[0] == key:
                db[streamerInformation[0]][1] = streamerInformation[2]
    elif commands == "StreamerOffline":
        for key in db.keys():
            if streamerInformation[0] == key:
                db.pop(streamerInformation[0])
    print(db)
    





    # return ["a", "b"]

val = True
while val:
    inp = [item for item in input("Enter input: ").strip().split(",")]
    print(inp)
    solution([inp[1], inp[2], inp[3]],inp[0]) 
