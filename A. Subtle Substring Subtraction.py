n = int(input())
for _ in range(n):
    s = input()
    p = 0
    if len(s)%2 == 0:
        for i in range(len(s)):
            if len(s)%2 == 0:
                p+=ord(s[i]) -96
                if i == len(s)-1:
                    print("Alice", p)
    else:
        if len(s) == 1:
            print("Bob", ord(s))
            continue
        else:
            for i in range(len(s)-1):
                p+=ord(s[i]) -96
                if p < ord(s[len(s)-1])%96 and i == len(s)-1:
                    print("Bob", ord(s[len(s)-1])%96 - p)
                else:
                    print("Alice", p-ord(s[len(s)-1])%96)
