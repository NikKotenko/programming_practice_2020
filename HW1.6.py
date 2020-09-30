max = 0
mid = 0
n = int(input())
while n != 0:
    if n > max:
        mid = max
        max = n
    if n < max and n >= mid:
        mid = n
    n = int(input())
print(mid)