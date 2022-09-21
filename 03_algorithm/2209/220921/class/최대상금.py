def change(i,n):
    global maxV
    if i == n:
        now = int(''.join(number))
        if now > maxV:
            maxV = now
    else:
        for q in range(len(number)):
            for w in range(q+1, len(number)):
                number[q], number[w] = number[w], number[q]
                if ''.join(number) not in visited[i]:
                    visited[i].append(''.join(number))
                    change(i+1, n)
                number[q], number[w] = number[w], number[q]

for tc in range(1, int(input())+1):
    number, cnt = input().split()
    number = list(number)
    cnt = int(cnt)
    maxV = 0
    visited = [[] for _ in range(cnt+1)]
    change(0,cnt)
    print(f'#{tc} {maxV}')