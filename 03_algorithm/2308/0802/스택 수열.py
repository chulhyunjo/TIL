N = int(input())
numbers = [int(input()) for _ in range(N)]
stack1 = [i for i in range(N, 0, -1)]
stack2 = []
answer = []
idx = 0

for i in range(N):
    stack2.append(stack1.pop())
    answer.append('+')

    while stack2 and stack2[-1] == numbers[idx]:
        stack2.pop()
        answer.append('-')
        idx += 1


if stack2:
    print('NO')
else:
    print(*answer, sep='\n')