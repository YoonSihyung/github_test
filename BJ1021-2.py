from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
target = list(map(int, input().split()))
queue = deque([i for i in range(1, n+1)]) #deque는 좌우로 입출력이 가능한 리스트이다.

task = 0

for i in target:
    while True:
        if queue[0] == i: #가장 왼쪽의 것을 제거하는 첫 번째 작업
            queue.popleft() #왼쪽의 것을 제거하는 popleft()함수
            break
        else:
            if queue.index(i) < len(queue)/2: #왼쪽으로 가는 거리가 짧은지, 오른쪽으로 가는 거리가 짧은지를 판단한다.
                while queue[0] != i:
                    queue.append(queue.popleft()) #가장 왼쪽것을 빼서 가장 오른쪽에 넣는다.
                    task += 1
            else:
                while queue[0] != i:c
                    queue.appendleft(queue.pop()) #가장 오른쪽것을 빼서 가장 왼쪽에 넣는다. deque만 가능한 appendleft() 함수.
                    task += 1

print(task)
