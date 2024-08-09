import sys
input = sys.stdin.readline

xa, ya, xb, yb, xc, yc = map(int, input().split())

if (yb-ya) * (xc-xa) == (yc-ya) * (xb-xa): #입력된 세 점이 삼각형을 만들지 못하고 일직선상에 있을 때
    print(float(-1))
else:
    sides = [((yb-ya)**2+(xb-xa)**2)**0.5, ((yc-yb)**2+(xc-xb)**2)**0.5, ((ya-yc)**2+(xa-xc)**2)**0.5]
    sides.sort() #세 점중 두 점을 골라 생기는 두 변의 길이를 작은 순서대로 나열

    #평행사변형은 만들어지는 세 선분 중 한 선분이 대각선이 되고, 나머지 두 선분은 평행사변형의 두 변이 된다.
    #이 때, 평행사변형의 둘레는 나머지 두 선분 길이의 두 배가 된다.
    mln = (sides[0]+sides[1])*2 #가장 작은 평행사변형은 작은 것들끼리 만들면 된다.
    mxx = (sides[1]+sides[2])*2 #가장 큰 평행사변형은 큰 것들끼리 만들면 된다.

    print(mxx-mln)