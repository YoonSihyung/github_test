import sys
input = sys.stdin.readline

lst = ['black\n', 'brown\n', 'red\n', 'orange\n', 'yellow\n', 'green\n', 'blue\n', 'violet\n', 'grey\n', 'white\n']

x = lst.index(input())
y = lst.index(input())
z = lst.index(input())

print((10 * x + y) * (10**z))