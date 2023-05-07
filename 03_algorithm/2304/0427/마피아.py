n = int(input())
guiltiness = list(map(int,input().split()))
members = [list(map(int,input().split())) for _ in range(n)]
R = int(input())
answer = 0
dead = [False] * n

def playGame(left, round):
    global answer, guiltiness

    if left == 1: # 마지막까지 남으면 그게 최대이므로 종료
        print(round)
        exit(0)

    if left % 2: # 홀 수일 때
        max_idx = 0
        max_guilt = -500
        for guilt in range(n):
            if guiltiness[guilt] > max_guilt and not dead[guilt]:
                max_guilt = guiltiness[guilt]
                max_idx = guilt
        if max_idx == R: # 마피아 일 경우 return
            answer = max(round, answer)
            return

        dead[max_idx] = True
        playGame(left-1, round)
        dead[max_idx] = False

    else:
        for j in range(n):
            if j == R or dead[j]:
                continue
            dead[j] = True
            for k in range(n):
                if not dead[k]:
                    guiltiness[k] += members[j][k]
            playGame(left-1, round+1)
            for k in range(n):
                if not dead[k]:
                    guiltiness[k] -= members[j][k]
            dead[j] = False


playGame(n,0)
print(answer)