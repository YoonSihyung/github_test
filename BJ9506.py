import sys

while True:
    n = int(sys.stdin.readline())

    if n == -1:
        break

    factors = []
    
    for i in range(1, n):
        if n % i == 0:
            factors.append(i)

    if sum(factors) == n:
        print(n, '=', end = ' ')
        print(' + '.join(map(str, factors)))
    else:
        print(n, 'is NOT perfect.')