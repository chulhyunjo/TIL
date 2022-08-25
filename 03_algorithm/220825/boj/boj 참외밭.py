n = int(input())
w = []
h = []
cnt = 0
for _ in range(6):
    a, b = map(int,input().split())
    if a in [1,2]:
        w.append([cnt,b])
    if a in [3,4]:
        h.append([cnt,b])
    cnt += 1

w.sort(key = lambda x: x[1])
h.sort(key = lambda x: x[1])
maxw = w[-1][1]
maxw_idx = w[-1][0]
maxh = h[-1][1]
maxh_idx = h[-1][0]

minush_idx = abs(5 - maxh_idx - 1)
minusw_idx = abs(5 - maxw_idx - 1)
for i in w:
    if i[0] == minusw_idx:
        minusw = i[1]
for j in h:
    if j[0] == minush_idx:
        minush = j[1]

area = maxw * maxh
minus_area = minusw * minush
print((area - minus_area)*n)
