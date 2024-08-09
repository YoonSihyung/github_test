import sys
input = sys.stdin.readline

n, m = map(int, input().split())
price = list(zip(*[list(map(int, input().split())) for _ in range(m)]))

if min(price[0]) < min(price[1]) * 6:
    print(min((min(price[0]) * (n//6)) + (min(price[1]) * (n%6)), (min(price[0]) * ((n//6) + 1))))
else:
    print(min(price[1]) * n)
