alphabets = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

n, b = input().split()
n = n[:][::-1]
result = 0

for i in range(len(n)):
    result += (alphabets.index(n[i])) * (int(b)**i)

print(result)