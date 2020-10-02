s = [int(s) for s in input().split()]
c = 0
for i in range(len(s)):
    for j in range(len(s)):
        if s[i] == s[j]:
            c+=1
    if c == 1:
        print(s[i])
    c=0
