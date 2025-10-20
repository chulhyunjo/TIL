TC = int(input())

for i in range(TC):
    a, b = input().split()
    count = [0] * 26
    for j in a:
        count[ord(j) - 97] += 1
    for j in b:
        count[ord(j) - 97] -= 1

    if all(x == 0 for x in count): print("Possible")
    else: print("Impossible")