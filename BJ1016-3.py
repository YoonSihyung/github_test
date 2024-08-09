import sys
input = sys.stdin.readline

mini, maxi = map(int, input().split())
numbers = [1 for i in range(maxi-mini+1)]
max_square = int(maxi**0.5)

for i in range(2, max_square + 1):
    j = i ** 2
    tmp = (mini//j) * j
    
    while tmp <= maxi:
        if mini <= tmp and tmp <= maxi:
            numbers[tmp-mini] = 0
        tmp += j

print(sum(numbers))
