import sys
input = sys.stdin.readline

mini, maxi = map(int, input().split())
numbers = [1 for i in range(maxi-mini+1)] #적은 메모리 사용을 위해 숫자 자체를 이용하는 것이 아니라 인덱스를 이용한다.

max_square = int(maxi**0.5) #maxi보다 가장 큰 제곱수의 제곱근

for i in range(2, max_square+1): #홀수의 제곱으로 나누어 떨어지는 수는 따로 해줘야 한다.
    for j in range(len(numbers)):
        if (j+mini) % (i**2) == 0:
            numbers[j] = 0

print(sum(numbers))