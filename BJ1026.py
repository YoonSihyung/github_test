import sys
input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()
b.reverse()

result = [a[i]*b[i] for i in range(n)]

print(sum(result))
