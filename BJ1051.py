import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [input().rstrip() for _ in range(n)]
max = 1

for i in range(n-1):
    for j in range(m-1):
        for k in range(i+1, n):
            if matrix[i][j] == matrix[k][j] and k-i <= m-1-j:
                if matrix[i][j] == matrix[i][j+k-i] and matrix[k][j] == matrix[k][j+k-i]:
                    if max < (k-i+1) ** 2:
                        max = (k-i+1) ** 2

print(max)