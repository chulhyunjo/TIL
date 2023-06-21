word = list(input())
answer = set()
stack1 = []
stack2 = []
nums = 0
for i in range(len(word)):
    if word[i] == '(':
        stack1.append(i)
        nums += 1
    elif word[i] == ')':
        stack2.append((stack1.pop(),i))

def dfs(d):
    for j in range(d,nums):
        s1, s2 = stack2[j]
        word[s1] = ''
        word[s2] = ''
        answer.add(''.join(word))
        dfs(j+1)
        word[s1] = '('
        word[s2] = ')'
dfs(0)
print(*sorted(answer), sep='\n')