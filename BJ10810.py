import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [0 for i in range(n)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for l in range(i-1, j):
        lst[l] = k

print(i for i in lst)
