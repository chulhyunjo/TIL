N = int(input())

waters = list(map(int,input().split()))
waters.sort()

answer = (0,0)
sub = int(2e9 + 1)

s = 0
e = N-1

while s < e:
    if abs(waters[s] + waters[e]) < sub:
        sub = abs(waters[s] + waters[e])
        answer = (waters[s], waters[e])

    if waters[s] + waters[e] > 0:
        e -= 1
    elif waters[s] + waters[e] < 0:
        s += 1
    else:
        answer = (waters[s], waters[e])
        break
print(*sorted(answer))