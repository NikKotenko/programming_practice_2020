n = int(input())
c = n - n//1440*1440
print(c//60 , c - c//60*60)