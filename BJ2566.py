import sys
input = sys.stdin.readline

lst = []

for _ in range(9):
    lst.append(list(map(int, input().split())))

maxes =[]

for i in lst:
    maxes.append(max(i))

print(max(maxes))
print(maxes.index(max(maxes))+1, lst[maxes.index(max(maxes))].index(max(maxes))+1)