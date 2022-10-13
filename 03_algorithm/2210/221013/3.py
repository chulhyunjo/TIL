from itertools import permutations


N = int(input())
baseball = [list(map(int,input().split())) for _ in range(N)]
ace_except_baseball = list(range(1,9))
start_list = []
result = []
for i in permutations(ace_except_baseball,8):
    i += (0,)
    start_list.append(i)


for i in start_list:
    one_ = 0
    two_ = 0
    three_ = 0
    score = 0
    inning = 0
    out = 0
    kk = 5
    while inning < N:
        j = i[kk%9]
        if baseball[inning][j] == 0:
            out += 1
            if out == 3:
                inning += 1
                out = 0
                one_ = 0
                two_ = 0
                three_ = 0
        elif baseball[inning][j] == 1:
            score += three_
            three_ = two_
            two_ = one_
            one_ = 1
        elif baseball[inning][j] == 2:
            score += three_ + two_
            three_ = one_
            two_ = 1
            one_ = 0
        elif baseball[inning][j] == 3:
            score += three_ + two_ + one_
            three_ = 1
            two_ = 0
            one_ = 0
        elif baseball[inning][j] == 4:
            score += three_ + two_ + one_ + 1
            three_ = 0
            two_ = 0
            one_ = 0
        kk += 1


    result.append(score)

print(max(result))