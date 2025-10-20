import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    vps = input().strip()
    stack = []
    for i in vps:
        if(i == "("):
            stack.append(i)
        else:
            if len(stack) == 0:
                stack.append(i)
                break
            else:
                stack.pop()

    print("YES") if len(stack) == 0 else print("NO")