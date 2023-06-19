N = int(input())
numbers = list(map(int,input().split()))
cnt = [0] * (10**6+1)

for i in range(N):
    cnt[numbers[i]] += 1

answer = [-1]
stack = [numbers.pop()]

for _ in range(N-1):
    n = numbers.pop()

    while stack and cnt[stack[-1]] <= cnt[n]:
        stack.pop()

    if stack:
        answer.append(stack[-1])
    else:
        answer.append(-1)

    stack.append(n)

print(*answer[::-1])