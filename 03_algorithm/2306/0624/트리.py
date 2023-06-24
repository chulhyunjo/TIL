import sys
input = sys.stdin.readline

# 3,6,5,4,8,7,1,2
# 5,6,8,4,3,1,2,7
# 5,8,4,6,2,1,7,3
def order(preorder_list, inorder_list):
    if not preorder_list:
        return
    elif len(preorder_list) == 1:
        print(preorder_list[0], end=' ')
        return
    elif len(preorder_list) == 2:
        print(preorder_list[1], preorder_list[0], end=' ')
        return

    root_node = preorder_list[0]
    root_idx = 0
    for i in range(len(inorder_list)):
        if inorder_list[i] == root_node:
            root_idx = i
            break

    preorder_left = preorder_list[1:root_idx+1]
    inorder_left = inorder_list[:root_idx]
    order(preorder_left, inorder_left)

    preorder_right = preorder_list[root_idx+1:]
    inorder_right = inorder_list[root_idx+1:]
    order(preorder_right, inorder_right)

    print(preorder_list[0], end=' ')

for _ in range(int(input())):
    N = int(input())
    tree = [0] * (N+1)
    preorder_list = list(map(int,input().split()))
    inorder_list = list(map(int,input().split()))

    order(preorder_list, inorder_list)
    print()
