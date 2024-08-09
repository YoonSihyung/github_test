import sys
input = sys.stdin.readline

test_case = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def worm(x, y):
    queue = [(x, y)]
    matrix[x][y] = 0

    while queue:
        x, y = queue.pop(0)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx > (m-1) or ny < 0 or ny > (n-1):
                continue

            if matrix[nx][ny] == 1:
                matrix[nx][ny] = 0
                queue.append((nx, ny))

for _ in range(test_case):
    m, n, k = map(int, input().split())
    matrix = [[0] * n for _ in range(m)]
    number = 0

    for i in range(k):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                number += 1
                worm(i, j)

    print(number)

