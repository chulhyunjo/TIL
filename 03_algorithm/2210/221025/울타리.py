def find(arr):
    x1 = min(list(map(lambda x:x[0], arr)))
    x2 = max(list(map(lambda x:x[0], arr)))
    y1 = min(list(map(lambda x:x[1], arr)))
    y2 = max(list(map(lambda x:x[1], arr)))
    return (x1,x2,y1,y2)

def area(arr):
    x1,x2,y1,y2 = find(arr)
    if x2-x1==0 or y2-y1==0:
        return x2-x1+y2-y1
    return 2*(x2-x1+y2-y1)

def maxTree(arr):
    return max(list(map(lambda x: x[2], arr)))

def findPoint(arr):
    x1, x2, y1, y2 = find(arr)
    point = []
    for i in range(len(arr)):
         if arr[i][0] in (x1,x2) or arr[i][1] in (y1, y2):
             point.append(arr[i])
    return point

def dfs(d, arr, wood):
    global minV
    if d >= minV:
        return
    if area(arr) <= maxTree(arr)+wood:
        minV = d+1
        return
    for i in findPoint(arr):
        da = set(arr)
        now = set()
        now.add(i)
        new_arr=list(da - now)
        if wood+i[2]>= area(new_arr):
            minV = d+1
            break
        dfs(d+1, new_arr, wood+i[2])

n = int(input())
location = []
for _ in range(n):
    location.append(tuple(map(int,input().split())))
data = set(location)
minV = 40
dfs(0,location,0)
print(minV)