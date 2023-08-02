N = int(input())

sums = 1
s = 1
e = 1
answer = 0
while s <= e:
    if sums == N:
        answer += 1
        sums -= s
        s += 1

    if sums < N:
        e += 1
        sums += e

    if sums > N:
        sums -= s
        s += 1

print(answer)