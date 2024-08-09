n = int(input())
nongroup = 0

for _ in range(n):
    word = input()
    lst = [word[0]]

    for i in range(1, len(word)):
        if word[i] != word[i-1]:
            if word[i] in lst:
                nongroup += 1
                break

print(n - nongroup)
