# 골드4
# 별자리 만들기
import sys
import math
N = int(sys.stdin.readline())
T = [list(map(float, sys.stdin.readline().split())) for _ in range(N)]
graph = {i : i for i in range(1, N+1)}
depth = {i : 0 for i in range(1, N+1)}
result = 0

# union-find 알고리즘
def union(root, node, add_len):
    r = find(root)
    n = find(node)

    if r == n : return
    
    global result
    result += add_len

    if depth[r] < depth[n]:
        graph[r] = n
    else:
        graph[n] = r
        if depth[r] == depth[n]:
            depth[r] += 1

def find(n):
    if graph[n] == n:
        return n
    else:
        graph[n] = find(graph[n])
        return graph[n]

matrix = []
for i in range(N-1):
    for j in range(i+1, N):
        diff = math.sqrt((T[i][0]-T[j][0])**2 + (T[i][1]-T[j][1])**2)
        matrix.append([i, j, diff])

# mst 알고리즘
matrix.sort(key= lambda x : x[2])
for i in matrix: union(i[0]+1, i[1]+1, i[2])

print(f"{result:.2f}")
print(matrix)
"""
3
1.0 1.0
2.0 2.0
2.0 4.0
"""