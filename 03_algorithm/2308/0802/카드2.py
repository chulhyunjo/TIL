from collections import deque

N = int(input())

cards = [i for i in range(N,0,-1)]
queue = deque(cards)
while len(queue) > 1:
    queue.pop()
    queue.appendleft(queue.pop())

print(queue[0])
