alphabets = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

n, b = map(int, input().split())
result = ''

while n // b > 0:
    result += alphabets[n % b]
    n //= b
result += alphabets[n]

result = result[:][::-1]
print(result)