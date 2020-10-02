s=[int(i) for i in input().split()]
c=0
for i in range (1, len(s)-1):
    if s[i]>s[i+1] and s[i]>s[i-1]:
        c+=1
print(c)
