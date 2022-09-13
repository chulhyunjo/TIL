h = list()
for _ in range(9):
    h.append(int(input()))
x1 = x2 = 0
h.sort()
overflow_h = sum(h) - 100
for i in range(9):
    for j in range(i+1,9):
        if h[i] + h[j] == overflow_h:
            x1, x2 = h[i], h[j]
            h.remove(x1)
            h.remove(x2)
            break
    if x1 and x2:
        break
for m in range(7):
    print(h[m])