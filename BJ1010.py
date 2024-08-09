import sys
input = sys.stdin.readline

def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac = fac * i
    return fac

case_num = int(input())

for _ in range(case_num):
    n, m = map(int, input().split())
    
    m_comb_n = int(factorial(m) / factorial(m-n) / factorial(n))
    
    print(m_comb_n)


