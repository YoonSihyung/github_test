import sys
input = sys.stdin.readline

n = int(input())
heights = [int(i) for i in input().split()]
maxi = 0

for i in range(len(heights)):
    ls = 1000000000
    rs = -1000000000
    see = 0
    for j in range(i-1, -1, -1):
         if (heights[j]-heights[i])/(j-i) < ls:
             see += 1
             ls = (heights[j]-heights[i])/(j-i)
    ls = 1000000000
    rs = -1000000000
    for j in range(i+1, n):
        if (heights[j]-heights[i])/(j-i) > rs:
            see += 1
            rs = (heights[j]-heights[i])/(j-i)

    maxi = max(maxi, see)

print(maxi)