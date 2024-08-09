import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    change = int(input())
    quarter, dime, nickel, penny = 0, 0, 0, 0

    while change >= 25:
        change -= 25
        quarter += 1

    while change >= 10:
        change -= 10
        dime += 1

    while change >= 5:
        change -= 5
        nickel += 1
    
    while change >= 1:
        change -= 1
        penny += 1
    
    print(quarter, dime, nickel, penny)