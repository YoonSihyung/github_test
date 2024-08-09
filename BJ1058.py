import sys
input = sys.stdin.readline

n = int(input())
friends_matrix = [list(input().rstrip()) for _ in range(n)]
maxi = 0

for i in range(n): #i는 내 인덱스
    tmp_list = friends_matrix[i][:]
    tmp = list(filter(lambda x: friends_matrix[i][x] == 'Y', range(n)))
    for j in tmp: #j는 나랑 일촌 친구의 인덱스
        for k in range(n): #k는 나랑 일촌 친구를 순회하기 위한 인덱스
            if k == i:
                continue
            if friends_matrix[j][k] == 'Y' and friends_matrix[i][k] == 'N':
                tmp_list[k] = 'Y'
    my_friend = tmp_list.count('Y')
    maxi = max(maxi, my_friend)

print(maxi)