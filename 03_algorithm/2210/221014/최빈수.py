for tc in range(1, int(input())+1):
    input()
    score = [0]*101
    arr = list(map(int,input().split()))
    for i in range(1000):
        score[arr[i]]+=1
    maxscore = 0
    result = 0
    for j in range(100):
        if maxscore<=score[j]:
            maxscore = score[j]
            result = j
    print(f'#{tc} {result}')