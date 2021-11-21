# 실버2
# 트리의 부모 찾기
import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())

T = [[] for _ in range(N+1)]
parents = [0 for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    T[a].append(b)
    T[b].append(a)
parents[1] = 1

def dfs(curr, tree, parents):
    for node in tree[curr]:
        if parents[node] == 0:
            parents[node] = curr
            dfs(node, tree, parents)

dfs(1, T, parents)
for i in range(2, N+1):
    print(parents[i])
"""
7
1 6
6 3
3 5
4 1
2 4
4 7

12
1 2
1 3
2 4
3 5
3 6
4 7
4 8
5 9
5 10
6 11
6 12
"""