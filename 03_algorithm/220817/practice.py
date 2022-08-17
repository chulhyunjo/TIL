alp_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
# alp_list 요소와 겹치는 문자열을 'A'로 교환하여 저장
for j in alp_list:
    for i in range(len(word)):
        if word[i:i + len(j)] == j:
            word = word.replace(word[i:i + len(j)], 'A')
            i += len(j)

print(len(word))