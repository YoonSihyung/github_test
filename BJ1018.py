import sys
import re

input = sys.stdin.readline

n, m = map(int, input().split())

board = [input() for i in range(n)] #현재 가진 보드를 저장한다.
correction = [] #각 반복에서 몇 개의 오류가 있는지를 저장. 결과는 이 중 가장 작은 것이 될 것이다.

#보드에서 체스판을 한칸씩 옮기면서 그 경우에 오류가 몇 개 있는지 판단하고 저장한다. 그 중 가장 작은 것이 정답
for i in range(n-7): #n행의 보드에서 8행의 체스판을 옮겨야 하므로
    for j in range(m-7): #n열의 보드에서 8열의 체스판을 옮겨야 하므로
        err1 = 0 #왼쪽위가 B인 정답지와 비교하여 오류 갯수를 찾는다.
        err2 = 0 #왼쪽위가 W인 정답지와 비교하여 오류 갯수를 찾는다.
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'B':
                        err1 += 1
                    elif board[a][b] != 'W':
                        err2 += 1
                else:
                    if board[a][b] != 'W':
                        err1 += 1
                    elif board[a][b] != 'B':
                        err2 += 1
        
        correction.append(min(err1, err2))

print(min(correction))
