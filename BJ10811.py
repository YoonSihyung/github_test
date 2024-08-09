import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(range(1, n+1))

for _ in range(m):
    a, b = map(int, input().split())
    lst[a-1:b] = lst[a-1:b][::-1]

print(*lst)
