from collections import deque
A, B = map(int, input().split())

queue = deque()
queue.append((A,0))
answer = -1
while queue:
    num, time = queue.popleft()
    if num*2 == B or str(num)+'1' == str(B):
        answer = time + 2
        break
    if num*2 < B:
        queue.append((num*2, time+1))
    if int(str(num) + '1') < B:
        queue.append((int(str(num) + '1'),time+1))

print(answer)