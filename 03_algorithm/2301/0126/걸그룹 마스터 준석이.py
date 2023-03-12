n, m = map(int,input().split())
group = dict()
member_dict = dict()
for _ in range(n):
    group_name = input()
    members_num = int(input())
    for _ in range(members_num):
        member = input()
        group[group_name] = group.get(group_name,[]) + [member]
        member_dict[member] = group_name

for _ in range(m):
    m = input()
    n = int(input())
    if n == 1:
        print(member_dict[m])
    if n == 0:
        print(*sorted(group[m]), sep='\n')