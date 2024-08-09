import sys
input = sys.stdin.readline

case_num = int(input())

for _ in range(case_num):
    x, y = map(int, input().split())
    distance = y - x

    count = 0
    level = 1
    steps = 0

    while True:
        count += 1
        steps += level
        
        if steps >= distance:
            print(count)
            break
        
        if count % 2 == 0:
            level += 1
