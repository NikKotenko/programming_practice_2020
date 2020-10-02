a = [int(i) for i in input().split()]
imax = a.index(max(a))
imin = a.index(min(a))
a[imax], a[imin] = a[imin], a[imax]
print(' '.join([str(i) for i in a]))
