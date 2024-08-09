import sys

input = sys.stdin.readline

n, m = map(int, input().split())
target = list(map(int, input().split()))

queue = [i for i in range(1, n+1)]

task = 0
head = 0
tail = n-1

def task1():
    global head
    global tail

    del queue[head]

    if head == 0:
        tail = len(queue) - 2
    elif head == len(queue):
        head = 0


def task2():
    global head
    global tail
    global task
    tail = head
    
    if head == len(queue) - 1:
        head = 0
    else:
        head += 1

    task += 1

def task3():
    global head
    global tail
    global task
    head = tail

    if tail == 0:
        tail = len(queue) - 1
    else:
        tail -= 1

    task += 1

for i in target:
    if queue.index(i) >= head:
        if queue.index(i) - head > len(queue)//2:
            for j in range(len(queue) - (queue.index(i) - head)):
                task3()
            task1()
        else:
            for j in range(queue.index(i) - head):
                task2()
            task1()
    else:
        if head - queue.index(i) > len(queue)//2:
            for j in range(len(queue) - (head - queue.index(i))):
                task2()
            task1()
        else:
            for j in range(head - queue.index(i)):
                task3()
            task1()

print(task)