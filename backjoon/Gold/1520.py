# 골드4
# 내리막 길
import sys
sys.setrecursionlimit(10**6) # 백준 런타임에러
N, M = map(int, sys.stdin.readline().split())
T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DP = [[-1 for _ in range(M)] for _ in range(N)]
move_x = [0, 0, 1, -1]
move_y = [1, -1, 0, 0]

def dfs(x, y):
    if y == N - 1 and x == M - 1: return 1
    if DP[y][x] != -1: return DP[y][x]

    DP[y][x] = 0
    for i in range(4):
        next_x = x+move_x[i]
        next_y = y+move_y[i]

        if N > next_y >= 0 and M > next_x >= 0:
            if T[next_y][next_x] < T[y][x]:
                DP[y][x] = DP[y][x] + dfs(next_x, next_y) 
                
    return DP[y][x]

print(dfs(0, 0))
print(DP)
# print(T)
        

"""
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
"""