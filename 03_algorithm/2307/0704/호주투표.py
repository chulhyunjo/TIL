n = int(input())
names = [input() for _ in range(n)]
votes = [] # 1~1000 * n 배열
for _ in range(1000):
    try:
        a, *b = map(int,input().split())
        votes.append([a,*b])
    except:
        break

votes_num = len(votes)
fail = [0] * n
cnt = [0] * n
votes_cnt = [0] * (votes_num)

left = n

for i in range(votes_num):
    cnt[votes[i][0]-1] += 1
while left > 1:
    for i in range(votes_num):
        tmp = 0
        while fail[votes[i][votes_cnt[i]]-1]:
            votes_cnt[i] += 1
            tmp = 1
        if tmp:
            cnt[votes[i][votes_cnt[i]]-1] += 1

    minVote = 1001
    this_fail = []
    for i in range(n):
        if not fail[i] and minVote > cnt[i]:
            this_fail = [i]
            minVote = cnt[i]
        elif not fail[i] and minVote == cnt[i]:
            this_fail.append(i)
    failNum = len(this_fail)
    if failNum == left:
        break
    else:
        for i in this_fail:
            fail[i] = 1
    left -= failNum

for i in range(n):
    if not fail[i]:
        print(names[i])
