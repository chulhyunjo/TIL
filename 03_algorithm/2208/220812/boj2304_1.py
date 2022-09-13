import sys
input = sys.stdin.readline
n = int(input())
pos = []
height = []

for _ in range(n):
    l, h = map(int ,input().split())
    pos.append(l)
    height.append(h)

arr = [0] * (max(pos) + 1) + [0]
for i in range(n):
    arr[pos[i]] = height[i]

area = 0
maxV = max(height)
maxh = 0
for i in range(1, len(arr)-1):
    if arr[i] > maxh:
        maxh = arr[i]
    area += maxh
    if arr[i] == maxV:
        maxV = max(arr[i+1:])
        maxh = maxV

print(area)