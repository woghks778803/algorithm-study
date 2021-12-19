# 골드3
# 우주신과의 교감
import sys
import math
from collections import defaultdict
N, M = map(int, sys.stdin.readline().split())

graph = {i : i for i in range(1, N+1)}
depth = {i : 0 for i in range(1, N+1)}
point_diff = defaultdict(dict)
univer_len = 0
matrix = []

def union(root, node, add_len):
    r = find(root)
    n = find(node)

    if r == n : return

    global univer_len
    univer_len += add_len

    if depth[r] < depth[n]:
        graph[r] = n
    else:
        graph[n] = r

        if depth[r] == depth[n]:
            depth[r] += 1

def find(n):
    if graph[n] == n: return n
    else: return find(graph[n])

for i in range(N):
    # 우주신의 좌표를 저장한다
    x, y = map(int, sys.stdin.readline().split())
    matrix.append([x, y])

for i in range(M):
    # 이미 연결된 통로는 미리 union으로 통합한다
    a, b = map(int, sys.stdin.readline().split())
    union(a, b, 0)

# 모든 간선의 거리 저장
for i in range(len(matrix)):
    for j in range(i+1, len(matrix)):
        if i != j : 
            x_minus = matrix[j][0] - matrix[i][0]
            if matrix[i][0] > matrix[j][0]: x_minus = matrix[i][0] - matrix[j][0]
            y_minus = matrix[j][1] - matrix[i][1]
            if matrix[i][1] > matrix[j][1]: y_minus = matrix[i][1] - matrix[j][1]

            diff = math.sqrt(x_minus**2 + y_minus**2)
            point_diff[i][j] = diff
    
matrix = []
for i in point_diff:
    for j in point_diff[i]:
        matrix.append([i, j, point_diff[i][j]])
del point_diff

# 간선 거리 정렬
matrix.sort(key= lambda x : (x[2], x[1], x[0]))

# mst 알고리즘
for i in range(len(matrix)):
    union(matrix[i][0]+1, matrix[i][1]+1, matrix[i][2])

print(f"{univer_len:.2f}")


"""
4 1
1 1
3 1
2 3
4 3
1 4

4 1
1 1
3 1
3 4
4 3
1 4
"""