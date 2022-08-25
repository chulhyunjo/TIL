from collections import deque

n = int(input())
paper_input = list(map(int, input().split()))
paper = deque()
for val in paper_input:
    paper.append(val)
ball = deque()
for i in range(1, n+1):
    ball.append(i)
res = []
Top = 0

while len(ball) > 0:
    b = ball.popleft()
    r = paper.popleft()
    if Top < r:
        if Top != -1:
            r -= 1

    res.append(b)
    ball.rotate(-r)
    paper.rotate(-r)

print(*res)