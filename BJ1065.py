import sys
input = sys.stdin.readline

n = int(input())
result = 0

for i in range(1, n+1): #1부터 n까지의 모든 수를 확인한다. 그 수를 나타내는 변수 i
    if len(str(i)) == 1 or len(str(i)) == 2:
        result += 1
    else:
        d = int(str(i)[1]) - int(str(i)[0])
        han = True
        for j in range(1, len(str(i))): #숫자 i의 각 자리수를 나타내는 변수 j
            if int(str(i)[j]) - int(str(i)[j-1]) != d:
                han = False
                break

        if han:
            result +=1

print(result)
