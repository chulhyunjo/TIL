from collections import deque

N, K = map(int,input().split())
queue = deque([''] * N)
flag = 0
cnt = [0] * 26

for _ in range(K):
    S, alp = input().split()
    S = int(S)
    # S칸 회전
    queue.rotate(-S)

    # 현재 자리가 확인이 되었고 다른 알파벳이면 X
    if queue[0] and queue[0] != alp:
        flag = 1
        break

    # 현재 자리가 확인하지 않은 곳이면
    if not queue[0]:
        queue[0] = alp
        # 같은 알파벳이 존재하면 X
        if cnt[ord(alp) - 65]:
            flag = 1
            break
    cnt[ord(alp) - 65] += 1

if flag:
    print('!')
else:
    # 시계방향으로 출력, 확인이 안된 칸은 ?출력
    queue.rotate(-1)
    for i in range(N-1, -1, -1):
        if queue[i]:
            print(queue[i], end='')
        else:
            print('?', end='')