# 실버3
# 패션왕 신해빈
import sys
from collections import defaultdict
N = int(sys.stdin.readline())

for i in range(N):
    T_N = int(sys.stdin.readline())
    graph = defaultdict(int)
    
    for j in range(T_N): 
        name, part = map(str, sys.stdin.readline().split())
        if graph.get(part): graph[part] += 1
        else: graph[part] = 1
        
    result = 1
    for j in graph: result *= graph.get(j)+1
    print(result-1)

"""
2
3
hat headgear
sunglasses eyewear
turban headgear
3
mask face
sunglasses face
makeup face
"""