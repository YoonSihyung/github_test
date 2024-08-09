import sys
input = sys.stdin.readline

n, kim, lim = map(int, input().split())
players = [0 for i in range(n)] #인원수에 따라 리스트에 0을 채워 놓는다.
players[kim-1] = 1
players[lim-1] = 1 #김지민과 임한수는 1로 표시해 놓는다. 그 위치는 위에서 input된 것에 따라 결정.
rnd = 1 #김지민과 임한수가 몇 라운드에서 만나는지 알기 위함.
finish = False #loop가 끝나는 시점을 정하기 위함.

while True:
    for i in range(1, len(players), 2): #한 조에는 두 명이므로 홀수 인덱스만을 살핀다.
        if players[i] == players[i-1] == 1: #만약 한 조에 있는 두 명이 김지민과 임한수라면
            print(rnd) #라운드 수를 출력
            finish = True #loop를 종료
            break

    if finish == True: #loop를 종료한다.
        break

    for i in range(1, len(players), 2): #한 조에는 두 명이므로 홀수 인덱스만을 살핀다.
        if players[i] == 1: #만약 홀수 인덱스에 김지민이나 임한수가 있다면 승리해야 한다.
            players[i-1] = -1 #그러므로 같은 조에 있는 다른 사람이 탈락
        else:
            players[i] = -1 #-1이 되면 탈락하는 것이다

    temp_list = [i for i in players if i != -1]
    players = temp_list[:] #탈락자들을 리스트에서 빼는 것을 다른 리스트에 옮겼다가 다시 저장하는 것으로 표현.

    rnd += 1
