# 골드4
# 최소 스패닝 트리
import sys
sys.setrecursionlimit(10**6) # 백준 런타임에러
V, E = map(int, sys.stdin.readline().split())
T = [list(map(int, sys.stdin.readline().split())) for _ in range(E)]
graph = {i : i for i in range(1, V+1)}
depth = {i : 0 for i in range(1, V+1)}
cost = 0

# union-find 알고리즘
def union(root, child, add_cost):
    r = find(root)
    c = find(child)

    if r == c: return
    global cost
    cost += add_cost
    
    if depth[r] < depth[c]:
        graph[r] = c
    else:
        graph[c] = r

        if depth[r] == depth[c]: depth[r] += 1

def find(x):
    if graph[x] == x:
        return x
    else:
        return find(graph[x])

# mst 알고리즘
T.sort(key= lambda x : x[2])
for i in T:
    union(i[0], i[1], i[2])

print(cost)
# print(T)
# print(graph)
# print(depth)

"""
3 3
1 2 1
2 3 2
1 3 3
= 3

7 12
6 7 6
3 5 7
4 7 8
1 2 9
3 4 9
1 3 10
5 7 1
3 6 2
2 7 3
4 6 4
2 5 5
2 4 10
= 25

6 9
1 2 -1
1 4 -3
2 4 5
2 3 3
3 4 1
3 6 -10
4 6 -7
4 5 8
5 6 5
= -16

6 9
1 2 -1
4 5 8
1 4 -3
2 4 5
4 6 -7
5 6 5
2 3 3
3 4 1
3 6 -10

"""