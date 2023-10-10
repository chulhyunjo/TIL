import sys
input = sys.stdin.readline

N, M = map(int,input().split())
names = [('',-1)]
for _ in range(N):
    A, num = input().split()
    if names[-1][1] != int(num):
        names.append((A,int(num)))

cnt = len(names)
for _ in range(M):
    level = int(input())
    s = 1
    e = cnt-1
    answer = names[1][0]
    while s <= e:
        mid = (s+e)//2

        if names[mid][1] >= level:
            e = mid - 1
            answer = names[mid][0]
        else:
            s = mid + 1

    print(answer)