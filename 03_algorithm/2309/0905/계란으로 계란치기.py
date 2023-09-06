def play(idx, cnt):
    global answer, cnt2
    cnt2 += 1
    if idx == N:
        answer = max(cnt, answer)
        return
    if (N - idx) * 2 + cnt <= answer:
        return
    if visited[idx]:
        play(idx+1, cnt)
    else:
        if cnt == N-1:
            play(idx+1, cnt)
        for i in range(N):
            if i == idx or visited[i]: continue
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]
            if eggs[idx][0] <= 0:
                visited[idx] = True
                if eggs[i][0] <= 0:
                    visited[i] = True
                    play(idx+1, cnt + 2)
                    visited[i] = False
                else:
                    play(idx+1, cnt + 1)
                visited[idx] = False
            else:
                if eggs[i][0] <= 0:
                    visited[i] = True
                    play(idx+1, cnt + 1)
                    visited[i] = False
                else:
                    play(idx+1, cnt)
            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]

N = int(input())
eggs = [list(map(int,input().split())) for _ in range(N)]
visited = [False] * N
answer = 0
cnt2 = 0
play(0,0)
print(answer)
print(cnt2)