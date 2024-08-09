import sys
input = sys.stdin.readline

l = int(input())
sett = [int(i) for i in input().split()]
n = int(input())

sett.append(n)
sett.sort()

if len(sett) != len(set(sett)): #n이 들어갔을 때 중복되는 원소가 생겼다는 것은 n자체가 이미 집합에 포함되어 있다는 것이므로 좋은 구간은 없다.
    good = 0
else:
    pivot = sett.index(n)
    if pivot == 0:
        good = n * (sett[1]-n) - 1
    else:
        good = (n-sett[pivot-1]) * (sett[pivot+1]-n) -1

print(good)