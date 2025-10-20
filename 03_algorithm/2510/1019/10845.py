import sys
from collections import deque
input = sys.stdin.readline

queue = deque()
N = int(input().rstrip())

for _ in range(N):
    command = input().rstrip().split()
    if command[0] == "push":
        queue.append(command[1])
    if command[0] == "pop":
        print(queue.popleft() if queue else -1)
    if command[0] == "size":
        print(len(queue))
    if command[0] == "empty":
        print(0 if queue else 1)
    if command[0] == "front":
        print(queue[0] if queue else -1)
    if command[0] == "back":
        print(queue[-1] if queue else -1)