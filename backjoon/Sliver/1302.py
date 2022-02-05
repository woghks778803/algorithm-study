# 실버4
# 베스트셀러
from collections import defaultdict
N = int(input())
graph = defaultdict()

for _ in range(N):
    T = input()
    if graph.get(T): graph[T] += 1
    else: graph[T] = 1
    
a = sorted(graph.items(), key= lambda x: (-x[1], x[0]))
print(a[0][0])

"""
5
top
top
top
top
kimtop

9
table
chair
table
table
lamp
door
lamp
table
chair

11
table
chair
table
table
lamp
door
lamp
table
chair
abc
abc
"""