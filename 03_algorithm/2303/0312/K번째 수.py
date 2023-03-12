n = int(input())
k = int(input())

# k = 1 B=[1]
# k = 2 B=[1,2,2,4]
# k = 3 B=[1,2,2,3,4,6,6,9]

A = []
for i in range(1,n):
    for j in range(i,n):
        A.append(i*j)

print(A)