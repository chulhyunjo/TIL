import sys
n = int(sys.stdin.readline())

for _ in range(n):
    bracket = sys.stdin.readline()
    cnt = 0
    idx = 0
    while cnt >= 0 and idx < len(bracket):
        if bracket[idx] == '(':
            cnt += 1
        if bracket[idx] == ')':
            cnt -= 1

        idx += 1

    if cnt == 0:
        print('YES')
    else:
        print('NO')
