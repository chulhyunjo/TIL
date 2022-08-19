n = int(input())
line = list(range(n,0,-1))
temp = []

line_idx = 0
while line_idx < n:
    temp.append(line.pop())