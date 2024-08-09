import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

r1, c1, r2, c2 = map(int, input().split())
result = [[0 for _ in range(c2-c1+1)] for _ in range(r2-r1+1)]
total = (c2-c1+1) * (r2-r1+1)
id = 1
x = 0
y = 0
i = 1
level = 1

while total > 0:
    for _ in range(2): #각 레벨에서 두 번씩 하므로
        for _ in range(level): #레벨만큼 반복한다.
            if r1 <= x <= r2 and c1 <= y <= c2: #소용돌이를 도는데 목표하는 범위 내에 들어오면 숫자를 적는다.
                result[x-r1][y-c1] = i
                total -= 1
                m = i #결과 리스트의 최댓값을 알기 위해 계속 업데이트한다.
            x += dx[id]
            y += dy[id] #다음 이동 좌표를 지정한다.
            i += 1 #적지 않더라도 이동할 때마다 i는 커져야 한다.
        i = (i-1) % 4 #한 번의 레벨 작업이 끝날때마다 이동 방향을 바꿔줘야 한다. 리스트에서 순환하는 것을 나머지(%)를 이용하면 편하다.
    level += 1 #레벨을 두 번 반복했으면 레벨을 올려줘야 한다.

digit = len(str(m))

for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(result[i][j]).rjust(digit), end = ' ')
    print() #한 행을 적으면 줄변경을 해줘야 한다.