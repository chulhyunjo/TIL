import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * 1001
last_area = 0
for _ in range(n):
    i, h = map(int,input().split())
    arr[i] = h
    if i > last_area:
        last_area = i

max_height = max(arr)
height = 0
width = 0
area = 0
new_max_height = 1001
for j in range(1,1001):
    if j == last_area:
        area += (j - width) * height
        break

    elif arr[j] == max_height:
        area += max_height + (j - width) * height
        new_max_height = max(arr[j+1:])
        height = new_max_height
        width = j

    elif arr[j] > height:
        area += (j - width) * height
        height = arr[j]
        width = j

    elif arr[j] == new_max_height:
        area += (j - width) * height
        new_max_height = max(arr[j + 1:])
        height = new_max_height
        width = j


print(area)