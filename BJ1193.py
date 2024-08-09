x = int(input())
n = int(((1+8*x)**0.5-1)/2) - 1 if int(((1+8*x)**0.5-1)/2) == ((1+8*x)**0.5-1)/2 else int(((1+8*x)**0.5-1)/2)
a = x - n*(n+1)//2
b = n+2 - (x - n*(n+1)//2)

if n % 2 == 1:
    print(str(a) + '/' + str(b))
else:
    print(str(b) + '/' + str(a))