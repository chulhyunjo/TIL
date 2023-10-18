word = input()
n = len(word)
need = word.count('a')

a_cnt = 0
for i in range(need):
    if word[i] == 'a':
        a_cnt += 1

min_move = need-a_cnt
for i in range(n):
    if word[i] == 'a':
        a_cnt -= 1
    if word[(i+need)%n] == 'a':
        a_cnt += 1
    min_move = min(min_move, need - a_cnt)

print(min_move)