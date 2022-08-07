from collections import deque
import sys
queue = deque()

n = int(input())
for _ in range(n):
    command = sys.stdin.readline().split()
    if command[0] == 'push_front':
        queue.appendleft(command[1])

    if command[0] == 'push_back':
        queue.append(command[1])

    if command[0] == 'pop_front':
        if not queue: print(-1)
        else: print(queue.popleft())

    if command[0] == 'pop_back':
        if not queue: print(-1)
        else: print(queue.pop())

    if command[0] == 'size':
        print(len(queue))

    if command[0] == 'empty':
        if not queue : print(1)
        else: print(0)

    if command[0] == 'front':
        if not queue : print(-1)
        else: print(queue[0])

    if command[0] == 'back':
        if not queue : print(-1)
        else: print(queue[-1])