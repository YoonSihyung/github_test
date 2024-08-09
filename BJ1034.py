import sys

n, m = map(int, sys.stdin.readline().split())
table = []
for _ in range(n):
    table.append(sys.stdin.readline().rstrip())
k = int(sys.stdin.readline())

#홀짝성을 이용한다. 현재 상태에서 몇 번 실행해 만들 수 있는 켜진 행의 최대값을 구하고, 홀짝성을 이용한다.
#만약 3번의 작용으로 최대값을 만들 수 있다면 모든 홀수 번의 작용으로 똑같은 최대값이 가능하다.
#3번의 작용으로 최대값을 만들 수 있는데 만약 k가 홀수라면? 최대값이 정답(홀짝이 바뀌어도 동일하다)
#3번의 작용으로 최대값을 만들 수 있는데 만약 k가 짝수라면? 짝수에서의 최댓값을 찾아야 한다.
#즉 k가 짝수라면 짝수 최댓값만 찾으면 되고, k가 홀수라면 홀수 최댓값만 찾으면 된다.
#000을 채우기 위해 3번 움직였을 때, 다른 형태의 것들은 전부 깨진다.
#이 원리를 이용하면, 000, 001, 010, 011, 111 같은 어떤 행의 형태는 같은 것끼리는 전부 다같이 움직이고, 다른 형태는 전부 다르게 움직인다.
#즉 가장 많은 행이 분포하는 형태에 따라서 움직이고, 그것이 채워지려면 홀수번 움직여야 하는지, 짝수번 움직여야 하는지 판단, 또 k와의 대소를 판단.
#0의 개수로 판단한다. 0의 개수가 짝수개이면 짝수번 움직여야 하는 행, 홀수개이면 홀수번 움직여야 하는 행.
#그렇다면 list로 다루기보다는 그냥 받아서 dictionary로 다루면 빠르고 편하게 다룰 수 있을 것 같다.

shapes = {}
for i in table:
    moves = list(map(int, list(i))).count(0)
    if moves % 2 == k % 2 and moves <= k:
        if i in shapes:
            shapes[i] += 1
        else:
            shapes[i] = 1

if shapes:
    print(max(shapes.values()))
else:
    print(0)