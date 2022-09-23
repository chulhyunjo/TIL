def change2(lst, st, y_n):
    if y_n == 1:
        money = 0
        for j in range(1,len(lst)+1):
            money += lst[-j] * 2**(j-1)
        st.add(money)
    else:
        for i in range(len(lst)):
            lst[i] = 1 if lst[i] == 0 else 0
            change2(lst,st,1)
            lst[i] = 1 if lst[i] == 0 else 0

def change3(lst, st, y_n):
    if y_n == 1:
        money = 0
        for k in range(1,len(lst)+1):
            money += lst[-k] * 3**(k-1)
        st.add(money)
    else:
        for i in range(len(lst)):
            tmp = lst[i]
            for j in range(3):
                if j == tmp:
                    continue
                else:
                    lst[i] = j
                change3(lst,st,1)
                lst[i] = tmp

for tc in range(1,int(input())+1):
    N2 = list(map(int,input()))
    N3 = list(map(int, input()))
    set2 = set()
    set3 = set()
    change2(N2,set2,0)
    change3(N3,set3,0)
    result = (set2&set3).pop()
    print(f'#{tc} {result}')