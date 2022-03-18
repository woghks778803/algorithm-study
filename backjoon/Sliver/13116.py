# 실버4
# 30번
def find(n, arr):
    # 루트까지의 경로 값 저장 
    arr.append(tree[n])
    if tree[n] == n:
        return arr
    else:
        return find(tree[n], arr)

def parent_tree(root):
    dq = deque([root])
    while dq:
        node = dq.popleft()

        # 루트의 자식부터 자식 노드의 값에 부모 노드값 저장 (R, L의 이진 트리 구조로)
        for i in range(node*2, node*2+2):
            if 1 <= i <= 1023:
                tree[i] = node
                dq.append(i)

    return tree

if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline
    output = sys.stdout.write
    tree = {1:1}
    tree = parent_tree(1)

    T = int(input())
    for i in range(T):
        A, B = map(int, input().split())
        arr_a = [A]
        arr_b = [B]
        arr_a = find(A, arr_a)
        arr_b = find(B, arr_b)

        result = 0
        while arr_a and arr_b:
            pop_a = arr_a.pop()
            pop_b = arr_b.pop()
            if pop_a == pop_b: result = pop_b
            else: break

        output(str(result*10)+'\n')
        # print(arr_a, arr_b)

"""
5
33 79
7 15
7 14
9 15
1022 1023
"""