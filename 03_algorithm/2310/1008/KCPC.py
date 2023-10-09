import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, k, t, m = map(int,input().split())
    teams = [[0 for _ in range(k+1)] for _ in range(n+1)]
    cnt = [0] * (n+1)
    time = [0] * (n+1)

    for q in range(m):
        i, j, s = map(int,input().split())
        if teams[i][j] < s:
            teams[i][j] = s
        cnt[i] += 1
        time[i] = q

    my_team = sum(teams[t])
    rank = 1
    for i in range(1,n+1):
        if i == t: continue # 같은 팀은 x
        if sum(teams[i]) > my_team:
            rank += 1
        if sum(teams[i]) == my_team:
            if cnt[t] > cnt[i]:
                rank += 1
            elif cnt[t] == cnt[i]:
                if time[t] > time[i]:
                    rank += 1

    print(rank)