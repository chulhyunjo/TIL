x = int(input())
line = list(input())
line.reverse()                          # 줄을 앞에서부터 뽑아오도록 reverse
stack = []                              # 입장 대기석
result = []                             # 클럽 입장한 사람 목록

while line:
    M = result.count('M')               # 현재 클럽에 있는 남자의 수
    W = result.count('W')               # 현재 클럽에 있는 여자의 수
    stack.append(line.pop())            # 맨 앞의 사람을 stack(입장 대기석)에 넣는다

    if stack[-1] == 'M' and M - W == x: # 클럽안에 남자가 여자보다 x가 많고 다음 사람이 남자일때
        if line and line[-1] == 'W':    # 줄에 사람이 있고 여자면 여자를 먼저 클럽에 입장
            result.append(line.pop())
        else:                           # 남자면 더이상 들어갈 수 없다 break
            break

    elif stack[-1] == 'W' and W-M == x: # 클럽안에 여자가 남자보다 x가 많고 다음 사람이 여자일때
        if line and line[-1] == 'M':    # 줄에 사람이 있고 다음 사람이 남자일때 다음 여자부터 입장
            result.append(line.pop())
        else:                           # 여자라면 인원 차이나서 break
            break

    result.append(stack.pop())          # 대기석에 있는 사람 입장
                                        # 위에서 예외의 경우는 이미 break
print(len(result))