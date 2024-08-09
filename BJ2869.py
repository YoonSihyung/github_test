a, b, v = map(int, input().split())
temp = (v-a)/(a-b)
intemp = int(temp)
print(intemp + 1 if temp == intemp else intemp + 2)