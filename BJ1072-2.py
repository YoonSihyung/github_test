import sys
input = sys.stdin.readline

x, y = map(int, input().split())
z = y * 100 // x

if z == 99 or z == 100:
    print(-1)
else:
    standard = (x + z*x - 100*y) / (99 - z)
    
    if standard // 1 == standard:
        print(int(standard))
    else:
        print(int(standard)+1)