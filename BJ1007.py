import sys
from itertools import combinations
input = sys.stdin.readline 

test_case = int(input())

for _ in range(test_case):
    n = int(input())
    points = []
    
    for _ in range(n):
        pt = list(map(int, input().split()))
        points.append(pt)

    comb = list(combinations(points, len(points)//2))
    start = comb[:len(comb)//2]
    end = comb[len(comb)//2:]
    end.reverse() #combinations 함수 특성상 짝지어지는 것들이 처음과 끝 두번째와 마지막 두번째 ... 이렇게 대칭적으로 있으므로
    #같은 인덱스에서 보기 위해 end 리스트를 반대로 만든다.
    scalars = []

    for i in range(len(comb)//2): #여러 개의 시작점 집합들과 끝점 집합들을 짝지어서 하나씩 살피는 변수 i
        x_start_total = 0
        y_start_total = 0
        x_end_total = 0
        y_end_total = 0
        for j in start[i]: #하나의 벡터를 만드는 시작점을 살피는 변수 j
            x_start_total += j[0]
            y_start_total += j[1]
        for k in end[i]: #하나의 벡터를 만드는 끝점을 살피는 변수 k
            x_end_total += k[0]
            y_end_total += k[1]

        result_vector = (x_end_total-x_start_total, y_end_total-y_start_total)
        length = (result_vector[0]**2 + result_vector[1]**2) ** 0.5
        scalars.append(length)

    print(min(scalars))