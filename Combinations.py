import sys
from itertools import combinations
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
result = list(combinations(lst, n))

print(result)
