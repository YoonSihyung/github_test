import sys
input = sys.stdin.readline

n = int(input())
a = [int(i) for i in input().split()]
b = a.copy()

b.sort()

p = [-1 for i in range(n)]
q = [-1 for i in range(n)]

for i in range(n):
    if a.count(b[i]) == 1:
        p[a.index(b[i])] = i
        q[a.index(b[i])] = b[i]

    else:
        temp = list(filter(lambda x: a[x] == b[i], range(len(a))))
        p[temp[q.count(b[i])]] = i
        q[temp[q.count(b[i])]] = b[i]

print(' '.join(str(s) for s in p))