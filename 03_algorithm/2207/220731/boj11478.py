n = input()
result = set()
for i in range(0,len(n)):
    for j in range(1,len(n) - i+1):
        result.add(n[i:i + j])
print(len(result))