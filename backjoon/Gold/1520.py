# 골드4
# 내리막 길
import sys
sys.setrecursionlimit(10**6) # 백준 런타임에러

# dfs 알고리즘
def dfs(x, y):
    if y == N - 1 and x == M - 1: return 1
    # 초기값과 방문시 셋팅값이 다른이유는 재탐색 방지를 위해서이다
    if DP[y][x] != -1: return DP[y][x]
    DP[y][x] = 0
    
    for i in range(4):
        next_x = x+move[i][0]
        next_y = y+move[i][1]

        if N > next_y >= 0 and M > next_x >= 0:
            if T[next_y][next_x] < T[y][x]:
                DP[y][x] += dfs(next_x, next_y) 
                
    return DP[y][x]

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())
    T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    DP = [[-1 for _ in range(M)] for _ in range(N)]
    move = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    print(dfs(0, 0))
    
    # print(DP)
    # print(T)

"""
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
"""