from collections import deque

wheel = [deque(map(int, list(input()))) for _ in range(4)]
k = int(input())
move = [tuple(map(int, input().split())) for _ in range(k)]
# idx 2는 오른쪽 6은 왼쪽과 맞닿음

for num, der in move:
    num -= 1
    moving_wheel = [num]
    right = left = 1
    while True:
        y_n = 0

        if 0 <= num + right < 4:
            if wheel[num+right-1][2] != wheel[num + right][6]:
                moving_wheel.append(num + right)
                right += 1
                y_n = 1
        if 0 <= num - left < 4:
            if wheel[num-left+1][6] != wheel[num - left][2]:
                moving_wheel.append(num - left)
                left += 1
                y_n = 1

        if not y_n:
            break

    for m in moving_wheel:
        if (m + num) % 2:
            tmp = 1 if der == -1 else -1
        else:
            tmp = der
        wheel[m].rotate(tmp)

result = 0
score = [1, 2, 4, 8]
for idx, w in enumerate(wheel):
    if w[0] == 1:
        result += score[idx]
    else:
        continue
print(result)
