word = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in lst:
    word = word.replace(i,'*')
result = len(word)
print(result)