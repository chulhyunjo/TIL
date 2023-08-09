names = dict()
total = 0
while True:
    try:
        name = input()
        names[name] = names.get(name, 0) + 1
        total += 1
    except:
        break

for n in sorted(names):
    cnt = names[n]
    print(f'%s %.4f' %(n, cnt/total*100))