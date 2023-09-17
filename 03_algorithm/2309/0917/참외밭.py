import sys

K = int(sys.stdin.readline())

height = []
width = []
total = []
for i in range(6):
    dir, length = map(int, sys.stdin.readline().split())
    if dir == 1 or dir ==2:
        width.append(length)
        total.append(length)
    else:
        height.append(length)
        total.append(length)

bigbox = max(height) * max(width)

#세로최대값
maxhidx = total.index(max(height))
#가로최대값
maxwidx = total.index(max(width))

small1 = abs(total[maxhidx-1] - total[(maxhidx-5 if maxhidx == 5 else maxhidx +1)])

small2 = abs(total[maxwidx-1] - total[(maxwidx-5 if maxwidx == 5 else maxwidx +1)])
area = bigbox - (small1 * small2)
print(area*K)