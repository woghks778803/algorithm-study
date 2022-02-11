# 골드5
# 치킨 배달
from itertools import combinations
import sys

input = sys.stdin.readline
N, M = map(int,input().split())
data = [[int(i) for i in input().split()] for _ in range(N)]

home = []
chicken = []
for i in range(N):
    for j in range(N):
        if data[i][j] == 1: home.append((i,j))
        elif data[i][j] == 2: chicken.append((i,j))

_chicken = list(combinations(chicken,M))
ans = int(1e13)
for ch in _chicken:
    val = 0
    for h in home:
        dist = int(1e13)
        for c in ch: dist = min(abs(h[0]-c[0])+abs(c[1]-h[1]), dist)
        
        val += dist
    ans = min(val, ans)

print(ans)

"""
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2
"""