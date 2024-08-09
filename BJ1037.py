import sys
input = sys.stdin.readline

n = int(input())

real_factors = [int(i) for i in input().split()]

if n > 1:
    real_factors.sort()
    print(real_factors[0] * real_factors[-1])
else:
    print(real_factors[0] * real_factors[0])
