for tc in range(1,int(input())+1):
    n = list(map(int,input().split()))
    p1 = [n[i] for i in range(0,12,2)]
    p2 = [n[i] for i in range(1,12,2)]
    cnt1 = [0] * 10
    cnt2 = [0] * 10
    result = 0
    for i in range(6):
        cnt1[p1[i]] += 1
        cnt2[p2[i]] += 1
        if i < 2: continue
        r1 = r2 = 0
        for j in range(10):
            if cnt1[j]:
                if cnt1[j] == 3: r1 += 1
                elif j <= 7 and cnt1[j] >= 1 and cnt1[j+1] >= 1 and cnt1[j+2] >= 1:
                    r1 += 1
            if cnt2[j]:
                if cnt2[j] == 3: r2 += 1
                elif j <= 7 and cnt2[j] >= 1 and cnt2[j+1] >= 1 and cnt2[j+2] >= 1:
                    r2 += 1
        if r1 or r2: break
    if not r1 and r2: result = 2
    if r1: result = 1
    print(f'#{tc} {result}')