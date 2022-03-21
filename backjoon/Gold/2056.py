# 골드4
# 작업
import sys
from collections import defaultdict
input = sys.stdin.readline
N = int(input())
graph = defaultdict()
for i in range(1, N+1):
    temp = [int(i) for i in input().split()]

    graph[i] = temp[0]
    if temp[1] == 0: continue
    for j in temp[2:]:
        graph[i] = max(temp[0]+graph[j], graph[i])

print(max(graph.values()))
print(graph)

"""
7
5 0
1 1 1
3 1 2
6 1 1
1 2 2 4
8 2 2 4
4 3 3 5 6

5
1 0
1 0
1 0
1 0
1 0

5
6 0
3 0
3 2 1 2
1 1 1
1 2 3 4

5
4 0
3 1 1
4 
"""