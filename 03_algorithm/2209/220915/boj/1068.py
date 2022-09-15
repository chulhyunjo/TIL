from collections import deque

N = int(input())
par = list(map(int,input().split()))
k = int(input())
queue = deque()
queue.append(k)
par[k] = -1
while queue:
    x = queue.popleft()
    for i in range(N):
        if par[i] == x:
            par[i] = -1
            queue.append(i)
print(par)
if not k and len(set(par))== 1:
    print(0)
elif len(set(par)) == 1:
    print(1)
elif len(set(par)) == 2:
    print(2)
else:
    print(len(set(par))-1)