alp_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
# alp_list 요소와 겹치는 문자열을 'A'로 교환하여 저장
for i in range(len(word)):
    for j in alp_list:
        if word[i:i + len(j)] == j:
            word = word.replace(j, 'A')
            i += len(j)

print(len(word))