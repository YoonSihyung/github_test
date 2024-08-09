import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    change = int(input())
    quarter = change // 25
    change %= 25
    dime = change // 10
    change %= 10
    nickel = change // 5
    change %= 5
    
    print(quarter, dime, nickel, change)