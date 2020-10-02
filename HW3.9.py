c = {}
for i in range(int(input())):
    line = input().split()
    for word in line:
        c[word] = c.get(word, 0) + 1

mc = max(c.values())
mf = [k for k, v in c.items() if v == mc]
print(min(mf))