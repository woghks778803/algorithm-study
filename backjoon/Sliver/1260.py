# 실버2
# DFS와 BFS
import sys
from collections import defaultdict
from collections import deque

# dfs 알고리즘
def dfs(visit, next):
    global graph
    visit.append(next)
    for i in graph[next]:
        if i in visit:
            pass
        else:
            dfs(visit, i)
    return visit

# bfs 알고리즘
def bfs(start):
    deq = deque()
    visit = [start]
    deq.append(start)

    while len(deq) > 0:
        next = deq.popleft()

        for next in graph[next]:
            if next not in visit:
                visit.append(next)
                deq.append(next)

    return visit

N, M, V = map(int, sys.stdin.readline().split())

graph = defaultdict(list)
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[b].append(a)
    graph[a].append(b)

for i in graph: graph[i].sort()


visit = dfs([], V)
print(str(visit).replace("[","").replace("]","").replace(",",""))

visit = bfs(V)
print(str(visit).replace("[","").replace("]","").replace(",",""))


"""
4 5 1
1 2
1 3
1 4
2 4
3 4

5 5 3
5 4
5 2
1 2
3 4
3 1

7 7 3
5 4
4 7
5 2
5 6
1 2
3 4
3 1
"""