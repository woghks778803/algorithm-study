# 실버4
# 숫자 카드
N = int(input())
T = [i for i in input().split()]
M = int(input())
T_M = [i for i in input().split()]
graph = {i : 0 for i in T_M}

for i in T:
    if graph.get(i) != None: graph[i] = 1

for i in T_M: print(graph[i], end=" ")

"""
5
6 3 2 10 -10
8
10 9 -5 2 3 4 5 -10
"""