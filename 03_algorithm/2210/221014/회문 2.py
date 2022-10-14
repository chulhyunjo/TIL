for tc in range(1, 11):
    input()
    graph = [list(input()) for _ in range(100)]
    maxLength = 0
    new_graph = list(map(list,zip(*graph[::-1])))
    for i in range(100):
        for j in range(100):
            for k in range(maxLength,100):
                if j + k > 100: break
                if "".join(graph[i][j:j+k]) == ''.join(graph[i][j:j+k][::-1]):
                    maxLength = k
                if ''.join(new_graph[i][j:j+k]) == ''.join(new_graph[i][j:j+k][::-1]):
                    maxLength = k
    print(f'#{tc} {maxLength}')