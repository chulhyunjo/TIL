number = {'A':0, 'C':1, 'G':2, 'T':3}

S, P = map(int,input().split())
dna = input()
need = list(map(int,input().split()))
answer = 0
check = 0
needCheck = 0

for i in range(P):
    num = number.get(dna[i],-1)
    need[num] -= 1

for i in range(4):
    if need[i] <= 0:
        check += 1

if check == 4:
    answer += 1

for i in range(S-P):
    first = number.get(dna[i])
    nxt = number.get(dna[P+i])
    need[first] += 1
    if need[first] > 0:
        check -= 1
    need[nxt] -= 1
    if need[nxt] == 0:
        check += 1

    if check == 4:
        answer += 1

print(answer)