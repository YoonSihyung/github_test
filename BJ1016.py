import sys
import math
input = sys.stdin.readline

mini, maxi = map(int, input().split())

numbers = [i for i in range(mini, maxi+1)] #mini와 maxi 사이의 모든 수를 저장
max_square = int(math.sqrt(maxi)) #maxi보다 작은 가장 큰 제곱수의 제곱 되기 전 수를 구한다.

temp_list = [i for i in numbers if i % 4 != 0] #짝수 제곱수의 배수는 모두 4의 배수이기도 하므로 4로 나누어 떨어지는 수들을 제거
numbers = temp_list[:]

for i in range(3, max_square+1, 2): #3부터 max_square까지 모든 홀수의 제곱으로 나누어 떨어지는 수들을 리스트에서 제거한다.
    temp_list = [j for j in numbers if j % (i**2) != 0]
    numbers = temp_list[:]

print(len(numbers))