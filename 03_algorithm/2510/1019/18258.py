import sys
from collections import deque

input = sys.stdin.readline

N = int(input().rstrip())
queue = deque()

for _ in range(N):
    command = input().rstrip().split()
    if command[0] == "push_front":
        queue.appendleft(command[1])
    elif command[0] == "push_back":
        queue.append(command[1])
    elif command[0] == "pop_front":
        print(queue.popleft() if queue else -1)
    elif command[0] == "pop_back":
        print(queue.pop() if queue else -1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(0 if queue else 1)
    elif command[0] == "front":
        print(queue[0] if queue else -1)
    elif command[0] == "back":
        print(queue[-1] if queue else -1)
