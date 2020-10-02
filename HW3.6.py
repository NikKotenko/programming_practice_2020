n = [int(s) for s in input().split()]
ob = set()
for num in n:
    if num in ob:
        print('YES')
    else:
        print('NO')
        ob.add(num)
