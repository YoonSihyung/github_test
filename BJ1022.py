import sys
input = sys.stdin.readline

r1, c1, r2, c2 = map(int, input().split())

abmax = max(abs(r1), abs(c1), abs(r2), abs(c2))
margin = 2*abmax + 1 #주어진 네 수중 절댓값이 가장 큰 수를 기준으로 정사각형 소용돌이를 만들 것이다.
#소용돌이 정사각형의 한 변의 길이는 2n+1이므로 margin이라고 칭함.

matrix  = [[0]*margin for _ in range(margin)] #한변의 길이가 2n+1인 정사각형 이차원 리스트 만들기

#이제 (0,0)에서부터 시작해 소용돌이 모양으로 움직이면서 1, 2, 3...을 채울 것이다.
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0] #다음 움직임을 이 방향으로 해야 한다.

x = abmax
y = abmax #문제상 (0,0) 그러나 실제 matrix에서 정중앙의 좌표는 왼쪽과 같다.

level = 1 #이 움직임을 몇 번 해야 하는가?
stack = 0 #레벨에서 몇 번째 반복인지 파악하기 위함
pair = 0 #이 레벨의 작업을 다른 방향으로 두 번 했는지를 파악하기 위함
id = 0 #dx, dy의 인덱스

for i in range(1, margin**2 + 1):
    matrix[x][y] = i
    x += dx[id]
    y += dy[id] #이 다음 숫자를 넣을 곳을 지정
    stack += 1 #이 레벨의 작업을 한번 더 했다는 것을 표시

    if stack == level: #이 레벨의 작업을 모두 마쳤을 때
        if pair == 1: #이 레벨의 작업을 다른 방향으로 두 번 했을 때
            level += 1 #다음 레벨로 가야 한다.
            pair = 0 #변수 초기화
        else:
            pair += 1

        stack = 0 #변수 초기화

        if id == 3:
            id = 0
        else:
            id += 1 #다음 작업부터는 다른 방향으로 진행한다는 것을 표시

result = [[0]*(c2-c1+1) for _ in range(r2-r1+1)] #요구하는 크기의 이차원 리스트를 준비

for i in range(r1+abmax, r2+abmax+1):
    for j in range(c1+abmax, c2+abmax+1): #matrix에서 잘라낼 부분의 인덱스를 순회한다.
        result[i-(r1+abmax)][j-(c1+abmax)] = matrix[i][j] #result 리스트의 인덱스는 (0, 0)부터 시작해야 하므로 (x-(r1+margin), y-(c1+margin))

max_value = max(max(row) for row in result) #result에서 가장 큰 수
digit = len(str(max_value)) + 1 #가장 큰 수의 자릿수에 1을 더한다. 각 수는 공백으로 구분되어야 하기 때문.

for i in result:
    for j in range(len(i)):
        if j == 0:
            print(str(i[j]), end = '') #각 행의 첫 번째 수는 공백으로 시작하면 안 되므로 오른쪽 들여쓰기를 하지 않는다. 그러나 줄바꿈은 안되므로 end를 이용한다.
        elif j == len(i) - 1:
            print(str(i[j]).rjust(digit)) #각 행의 마지막 수는 줄바꿈을 해야 하므로 end를 사용하지 않는다.
        else:
            print(str(i[j]).rjust(digit), end = '') #나머지 수들은 공백으로 구분되고 줄바꿈을 하지 않으므로 digit만큼의 오른쪽 들여쓰기를 하지 않고 end를 이용한다.