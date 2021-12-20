# 골드1
# 행성 터널
import sys
sys.setrecursionlimit(10**6) # 백준 런타임에러
N = int(sys.stdin.readline())
T = []
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    T.append([x, y, z, i])
# T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

graph = {i : i for i in range(N)}
depth = {i : 0 for i in range(N)}
result = 0

# union-find 알고리즘
def union(root, node, add_len):
    r = find(root)
    n = find(node)
    if r == n: return

    # mst 알고리즘
    global result
    result += add_len

    if depth[r] < depth[n]:
        graph[n] = r
    else:
        graph[r] = n
        if depth[r] == depth[n]: depth[r] += 1

def find(n):
    if graph[n] == n: return n
    else:
        # 매번 함수 호출은 리소스 소모가 심하니 DP 처리
        graph[n] = find(graph[n]) 
        return graph[n]

matrix = []

# 받은 좌표값에서 x, y, z축별 오름차순으로 정렬 후 인접 정점의 거리 값만 저장 (각 축에서 가장 가까운 거리)
# 시간 복잡도 3(n-1)
T.sort(key= lambda x : x[0])
for i in range(1, N):
    matrix.append([T[i][3], T[i-1][3], abs(T[i][0]-T[i-1][0])])

T.sort(key= lambda x : x[1])
for i in range(1, N):
    matrix.append([T[i][3], T[i-1][3], abs(T[i][1]-T[i-1][1])])

T.sort(key= lambda x : x[2])
for i in range(1, N):
    matrix.append([T[i][3], T[i-1][3], abs(T[i][2]-T[i-1][2])])

#union-find + mst
matrix.sort(key= lambda x : x[2])
for i in range(len(matrix)):
    union(matrix[i][0], matrix[i][1], matrix[i][2])

print(result)
# print(matrix)
# print(T)
# print(graph)

# 모든 간선의 거리 구하기 - 최소 공식 적용 (min(|xA-xB|, |yA-yB|, |zA-zB|))
# 시간 복잡도 n(n+1)/2
# for start in range(N):
#     for end in range(start+1, N):
#         if start != end:
#             diff = min(abs(T[start][0]-T[end][0]), abs(T[start][1]-T[end][1]), abs(T[start][2]-T[end][2]))
#             matrix.append([start, end, diff])

# matrix.sort(key= lambda x : x[2])

"""
5
11 -15 -15
14 -5 -15
-1 -1 -5
10 -4 -1
19 -4 19
"""