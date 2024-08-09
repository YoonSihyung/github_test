import sys
from collections import deque

def DFS(v):
    queue = deque()
    queue.append(v)
    result = [v]

    while queue:
        back = True
        for i in graph[queue[-1]]:
            if i not in queue and i not in result:
                queue.append(i)
                result.append(i)
                back = False
                break
        if back:
            queue.pop()

    return result


def BFS(v):
    queue = deque()
    queue.append(v)
    result = []

    while queue:
        for i in graph[queue[0]]:
            if i not in queue and i not in result:
                queue.append(i)
        result.append(queue.popleft())

    return result


n, m, v = map(int, sys.stdin.readline().split())
graph = {}
for i in range(1, n+1):
    graph[i] = []

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph.keys():
    graph[i] = sorted(graph[i])

print(*DFS(v))
print(*BFS(v))