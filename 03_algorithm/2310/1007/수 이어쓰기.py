from collections import deque

N = deque(list(input()))

find = 0
while N:
    find += 1
    number = deque(list(str(find)))
    while N and number:
        if N[0] == number[0]:
            N.popleft()
        number.popleft()
print(find)