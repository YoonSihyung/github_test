import sys
input = sys.stdin.readline

x, y = map(int, input().split())

if x == y or y * 100 // x == 99:
    print(-1)
else:
    games = x + 1
    wins = y + 1
    while True:
        if (y * 100 // x) + 1 == wins * 100 // games:
            print(games - x)
            break
        else:
            games += 1
            wins += 1
