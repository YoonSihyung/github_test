n = int(input())
level = 1
margin = 1
d = 6

while margin < n:
    margin += d
    level += 1
    d += 6

print(level)