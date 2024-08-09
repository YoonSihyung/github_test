import sys
input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [input().rstrip() for _ in range(n)] #표 생성
maxi = -1

def sqr(s):
    s = int(s)
    return int(s**0.5)**2 == s

for i in range(n): #행 시작점을 이동시키면서 확인한다.
    for j in range(m): #열 시작점을 이동시키면서 확인한다.
        for dx in range(-n, n): #행 등차를 바꾸면서 확인한다.
            for dy in range(-m, m): #열 등차를 바꾸면서 확인한다.
                #여기서 범위가 -n과 -m에서 시작하는 이유는 n과 m이 1인 경우에 한 번은 진행시켜야 하기 때문이다.
                #다른 경우에는 -n과 -m부터 시작하면 어차피 범위 밖으로 벗어나는데, n과 m이 1인 경우에는 -n+1과 -m+1부터 시작하면 dx와 dy가
                #0 한번만 되므로 아래 if문에 의하여 아무것도 할 수 없게 된다. 이에 따라 한 번 완전제곱수 판단을 하기 위해 -n, -m부터 시작한다.
                s = ''
                x, y = i, j

                if dx == 0 and dy == 0: #x와 y가 변해야 루프도 끝나기 때문에 0인 경우는 하지 않는다.
                    continue
                
                while 0 <= x <= n-1 and 0 <= y <= m-1:
                    s += matrix[x][y] #s에 숫자를 하나씩 넣는다. 그러면 길이는 다르지만 등차수열 규칙에는 맞는 수들을 전부 검사할 수 있다.
                    
                    if sqr(s) : #s가 완전제곱수인지를 판단한다.
                        maxi = max(int(s), maxi)
                
                    x += dx
                    y += dy

print(maxi)