def solution(numbers, target):
    answer = 0

    def dfs(depth, nowAdd):
        if nowAdd == target:
            return 1
        elif nowAdd > target:
            return 0

        if depth < nums:
            result = 0
            result += dfs(depth + 1, nowAdd + numbers[depth])
            result += dfs(depth + 1, nowAdd - numbers[depth])
            result += dfs(depth + 1, nowAdd)
            return result
        else:
            return 0

    nums = len(numbers)
    answer = dfs(0, 0)
    return answer

n = [1,1,1,1,1]
t = 3
print(solution(n,t))