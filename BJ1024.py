import sys
input = sys.stdin.readline

n, l = map(int, input().split())
condition = False

for i in range(l, 101):
    if i % 2 == 1: #만약 i가 홀수인 경우
        if n % i == 0 and int((n/i) - (i//2)) >= 0: #n이 어떤 수 i로 나누어 떨어질 때, 결과값 수열의 가장 작은 값이 0 이상일 때,
            result = [j for j in range(int((n/i) - (i//2)), int((n/i) + (i//2) + 1))] #n/i를 중심으로 연속된 수는 n/i - i//2부터 n/i + i//2까지 홀수개
            print(' '.join(str(s) for s in result))
            condition = True
            break

    else:
        if (n / i) % 1 == 0.5 and int((n/i) - (i//2) + 0.5) >= 0: #n이 어떤 수 i로 나누어서 .5 형태가 나올 때, 결과값 수열의 가장 작은 값이 0 이상일 때,
            result = [j for j in range(int((n/i) - (i//2) + 0.5), int((n/i) + (i//2) + 0.5))] # n/i를 중심으로 연속된 수는 n/i - i//2 + 0.5부터 n/i + i//2 - 0.5까지 짝수개
            print(' '.join(str(s) for s in result))
            condition = True
            break

if condition == False:
    print(-1)