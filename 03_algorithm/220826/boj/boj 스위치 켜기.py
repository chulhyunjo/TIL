n = int(input())
light = list(map(int,input().split()))
m = int(input())
for _ in range(m):
    s, num = map(int,input().split())
    idx = num -1 # 인덱스
    if s == 1:
        for i in range(idx,len(light),num):
            if light[i]:
                light[i] = 0
            else:
                light[i] = 1

    if s == 2:
        left = 0
        right = 0
        while idx-left >= 0 and idx+right < n and light[idx-left] == light[idx+right]:
            left += 1
            right += 1
        if not left and not right:
            left = idx
            right = idx
        else:
            left = idx - (left - 1)
            right = idx + (right - 1)

        for j in range(left, right+1):
            if light[j]:
                light[j] = 0
            else:
                light[j] = 1

for q in range(0,len(light), 20):
    print(*light[q:q+20])