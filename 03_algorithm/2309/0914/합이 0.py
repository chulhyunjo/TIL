def check(a, b, c, a_cnt, b_cnt, c_cnt):
    if a == b == c:
        return a_cnt * (a_cnt - 1) * (a_cnt - 2) // 6
    elif b == c:
        return a_cnt * (b_cnt * (b_cnt-1) // 2)
    elif a == b:
        return (a_cnt * (a_cnt-1)//2) * c_cnt
    else:
        return a_cnt * b_cnt * c_cnt


N = int(input())
numbers = list(map(int,input().split()))
numbers_cnt = dict()
for i in range(N):
    num = numbers[i]
    numbers_cnt[num] = numbers_cnt.get(num,0) + 1

answer = 0
numbers = sorted(set(numbers))
M = len(numbers)
if M == 1:
    if numbers[0] == 0:
        print(N*(N-1)*(N-2)//6)
    else:
        print(0)
else:
    for i in range(M-1):
        a = numbers[i]
        a_cnt = numbers_cnt[a]
        s = i
        e = M - 1

        while s <= e:
            b = numbers[s]
            c = numbers[e]
            if a == b:
                if a_cnt == 1:
                    s += 1
                    continue
            if b == c:
                if numbers_cnt[b] == 1:
                    break
            sum1 = a + b + c
            if sum1 > 0:
                e -= 1
            elif sum1 < 0:
                s += 1
            else:
                b_cnt = numbers_cnt[b]
                c_cnt = numbers_cnt[c]
                cnt = check(a, b, c, a_cnt, b_cnt, c_cnt)
                answer += cnt
                s += 1
    print(answer)