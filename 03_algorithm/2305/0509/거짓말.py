N, M = map(int,input().split()) # N: 사람의수 M: 파티의 수
parent = list(range(N+1))

def find(x):
    if x == parent[x]:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

knowNums, *people = map(int, input().split()) # 거짓말인지 아는 사람의 수, 그룹

partyInfo = []
for _ in range(M):
    nums, *party = list(map(int, input().split()))
    partyInfo.append(party)

for i in range(M):
    if len(partyInfo[i]) == 1:
        continue
    else:
        for j in range(1,len(partyInfo[i])):
            union(partyInfo[i][0], partyInfo[i][j]) # 같은 파티에 참여한 사람

answer = 0
for i in range(M):
    isPossible = True
    firstPerson = partyInfo[i][0]
    for j in range(knowNums):
        if find(firstPerson) == find(people[j]):
            isPossible = False
            break
    if isPossible:
        answer += 1

print(answer)