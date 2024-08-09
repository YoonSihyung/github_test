n = open(0).read().split()
print(n[i:=n.index(max(n, key = int))], i//9 + 1, i%9 + 1)
