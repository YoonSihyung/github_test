grade = ['F', 'E', 'D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+'] 
dividend = 0
divisor = 0

for _ in range(20):
    a, b = input().split()[1:]
    
    if b == 'P':
        continue
    else:
        dividend += float(a) * grade.index(b) * 0.5
        divisor += float(a)

print(dividend / divisor)
