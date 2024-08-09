lst = []

for _ in range(5):
    lst.append(list(input()))

length = 0
for i in lst:
    length += len(i)

i = 0
result = ''
while length:
    if len(lst[i]):
        result += lst[i].pop(0)
        length -= 1
    
    if i == len(lst) - 1:
        i = 0
    else:
        i += 1

print(result)