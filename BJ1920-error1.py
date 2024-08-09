import sys

n = int(sys.stdin.readline())
lst1 = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
lst2 = list(map(int, sys.stdin.readline().split()))

for i in lst2:
    result = 0
    find = lst1[:]

    while len(find) > 1:
        if find[n//2] == i:
            result = 1
            break
        elif find[n//2] > i:
            find = find[:n//2-1]
            n //= 2
        elif find[n//2] < i:
            find = find[n//2+1]
            n //= 2

    print(result)