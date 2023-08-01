N = int(input())
ans = []
for i in range(N):
    ans.append(int(input()))
ans.sort()

print(*ans, sep='\n')