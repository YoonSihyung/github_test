import sys
input = sys.stdin.readline

s, n, k, r1, r2, c1, c2 = map(int, input().split())
l = n**s

def black(x, y, l):
    center = l//n
    if l == 1:
        return 0
    elif center * (n-k)//2 <= x < center * (n+k)//2 and center * (n-k)//2 <= y < center * (n+k)//2:
        return 1
    x %= center
    y %= center
    return black(x, y, l//n)

for i in range(r1, r2+1):
    for j in range(c1, c2+1):
        print(black(i, j, l), end = '')
    print()