import sys
input = sys.stdin.readline

n = int(input()) # 1~n까지의 수
su = [int(input()) for _ in range(n)] # 만들어야 하는 수열 리스트

nums = list(range(n,0,-1)) # 1~n까지의 수를 반대로 담은 stack
stack = [] # 1~n까지의 수를 순서대로 담고 꺼내서 수열을 만들 stack

result = '' # 최종 출력 결과 담을 변수
cnt = 0 # 수열의 수와 같을 때 카운트 해서 index확인
while cnt < n:
    stack.append(nums.pop())
    result += '+'

    while stack and stack[-1] == su[cnt]:
        stack.pop()
        cnt += 1
        result += '-'

    if not nums and stack and stack[-1]> su[cnt]:
        result = 'NO'
        break

if result == 'NO':
    print(result)
else:
    for i in result:
        print(i)