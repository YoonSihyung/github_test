from collections import deque

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    d = list(map(int, input().split()))
    graph = [[] for j in range(n + 1)]
    inDegree = [0 for j in range(n + 1)]
    dp = [0 for j in range(n + 1)]
    queue = deque()

    for j in range(k):
        a, b = map(int, input().split())
        graph[a].append(b)
        inDegree[b] += 1

    w = int(input())

    for j in range(1, n + 1):
        if inDegree[j] == 0:
            queue.append(j)
            dp[j] = d[j - 1]
    
    while queue:
        tmp = queue.popleft()

        for j in graph[tmp]:
            inDegree[j] -= 1
            dp[j] = max(dp[j], dp[tmp] + d[j - 1])
            if inDegree[j] == 0:
                queue.append(j)

    print(dp[w])
