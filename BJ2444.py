n = int(input())

for i in range(n):
    a = ' ' * (n-i) + '*' * (2*i+1)
    print(a)

for i in range(n-2, -1, -1):
    a = ' ' * (n-i) + '*' * (2*i+1)
    print(a)
