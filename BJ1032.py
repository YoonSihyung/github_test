import sys
input = sys.stdin.readline

n = int(input())
files = []

for _ in range(n):
    files.append(input().rstrip())

result = ''
diff = False

for i in range(len(files[0])):
    for j in range(len(files) - 1):
        if files[j][i] != files[j+1][i]:
            diff = True
        
    if diff:
        result += '?'
    else:
        result += files[0][i]

    diff = False

print(result)
