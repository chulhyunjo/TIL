from collections import deque
import copy

n = int(input())
arr = deque(list(map(int,input().split())))
make = deque(list(map(int,input().split())))
make_re = make.copy()
make.reverse()

for _ in range(n):
    arr.rotate(1)
    if arr == make or arr == make_re:
        print('good puzzle')
        break

else:
    print('bad puzzle')
