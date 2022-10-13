def comb(d, l):
    if d == k:
        spin(graph, l)
    else:
        for i in range(k):
            if not used[i]:
                used[i] = 1
                comb(d+1, l+[combination[i]])
                used[i] = 0


def spin(arr, com):
    global result
    new_arr = [ar[:] for ar in arr]
    for co in com:
        r, c, s = co[0]-1, co[1]-1, co[2]
        startx, starty = (r-s, c-s)
        endx, endy = (r+s, c+s)
        next_arr = [a[:] for a in new_arr]
        while startx < endx and starty < endy:
            for i in range(starty+1, endy+1):
                next_arr[startx][i] = new_arr[startx][i-1]
            for i in range(startx+1, endx+1):
                next_arr[i][endy] = new_arr[i-1][endy]
            for i in range(endy-1, starty-1, -1):
                next_arr[endx][i] = new_arr[endx][i+1]
            for i in range(endx-1, startx-1,-1):
                next_arr[i][starty] = new_arr[i+1][starty]
            startx += 1
            starty += 1
            endx -= 1
            endy -= 1
            new_arr = [a[:] for a in next_arr]
    for line in new_arr:
        result = min(sum(line), result)

n, m, k = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
combination = [list(map(int,input().split())) for _ in range(k)]
used = [0] * k
result = 5000
comb(0,[])
print(result)