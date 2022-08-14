def solution(id_list, report, k):
    answer = []
    counts = [0] * len(id_list)
    ban = dict()
    for i in range(len(report)):
        key, value = report[i].split()
        if key in ban.keys():
            ban[key] += [value]
        else:
            ban[key] = [value]

    print(ban)

    return answer


id_list = ['muzi', 'frodo', 'apeach', 'neo']
report = ['muzi frodo', 'apeach frodo', 'frodo neo', 'muzi neo', 'apeach muzi']
k = 2

print(solution(id_list, report, k))