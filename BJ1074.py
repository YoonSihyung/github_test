import sys
input = sys.stdin.readline

n, r, c = map(int, input().split())

def what4(n, r, c):
    if r+1 > 2**(n-1) and c+1 > 2**(n-1):
        return 3
    elif r+1 > 2**(n-1) and c+1 <= 2**(n-1):
        return 2
    elif r+1 <= 2**(n-1) and c+1 > 2**(n-1):
        return 1
    else:
        return 0
#가장 큰 단위부터 어떤 사분면에 속하는지, 단위를 하나씩 줄여가면서 계속 어떤 사분면에 속하는지 판단하여 숫자를 찾아나간다.
#나머지를 이용해 사분면이 달라서 숫자가 다르더라도 동일하게 다룰 수 있도록 한다.
#예시: 3 6 3 - 45 row7col4

result = 0

for i in range(n, 0, -1):
    result += what4(i, r, c) * 2**((i-1)*2)
    r %= 2**(i-1)
    c %= 2**(i-1)

print(result)