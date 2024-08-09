paper = [[0] * 100 for i in range(100)]

n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    
    for i in range(a-1, a+9):
        for j in range(b-1, b+9):
            paper[i][j] = 1

result = 0

for i in range(100):
    result += paper[i].count(1)

print(result)