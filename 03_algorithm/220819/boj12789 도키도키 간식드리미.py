n = int(input())
line = list(map(int,input().split()))
line.reverse()
temp = []
result = list(range(1,n+1))
line_idx = 0
while line:
    temp.append(line.pop())

    while temp and temp[-1] == result[line_idx]:
        line_idx += 1
        temp.pop()

    if not line and temp and temp[-1] > result[-1]:
        break

if temp:
    print("Sad")
else:
    print("Nice")