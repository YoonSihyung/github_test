import sys
input = sys.stdin.readline

n = int(input())
f = int(input())

n -= (n % 100)

while True:
    if n % f == 0:
        print(str(n)[-2:])
        break
    n += 1