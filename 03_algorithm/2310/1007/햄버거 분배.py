from collections import deque

N, K = map(int,input().split())
line = list(input())

hamburger = deque()
people = deque()

answer = 0
for i in range(N):
    if hamburger and hamburger[0] < i-K:
        hamburger.popleft()
    if people and people[0] < i-K:
        people.popleft()
        
    if line[i] == 'H':
        if people:
            people.popleft()
            answer += 1
        else:
            hamburger.append(i)
    else:
        if hamburger:
            hamburger.popleft()
            answer += 1
        else:
            people.append(i)

print(answer)