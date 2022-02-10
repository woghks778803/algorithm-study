# 골드1
# 구간 합 구하기
def init(start, end, node):
    if start == end: 
        tree[node] = T[start-1]
        return tree[node]

    mid = (start+end) // 2
    tree[node] = init(start, mid, node*2) + init(mid+1, end, node*2 + 1)
    return tree[node]

def sum(start, end, node, left, right):
    if left > end or right < start: return 0
    if left <= start and end <= right: return tree[node]

    mid = (start+end) // 2
    
    return sum(start, mid, node*2, left, right) + sum(mid+1, end, node*2 + 1, left, right)

def update(start, end, node, idx, dif):
    
    if idx > end or idx < start: return
    tree[node] += dif
    if start == end: return
    mid = (start+end) // 2
    update(start, mid, node*2, idx, dif)
    update(mid+1, end, node*2+1, idx, dif)

if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N, M, K = map(int, input().split())

    T = [int(input()) for _ in range(N)]
    tree = {}
    init(1, N, 1)
    
    for i in range(M+K):
        a, b, c = map(int, input().split())
        if a == 1:
            dif = c - T[b-1]
            T[b - 1] = c
            update(1, N, 1, b, dif)
        else:
            print(sum(1, N, 1, b, c))

    # print(T)
    # print(tree)

"""
5 2 2
1
2
3
4
5
1 3 6
2 2 5
1 5 2
2 3 5
"""