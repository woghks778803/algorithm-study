# 골드5
# 적록색약
def in_scope(x, y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def merge_rg(arr):
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'R': arr[i][j] = 'G'
    return arr

def dfs(standard_arr, standard_val, x, y):
    if visited[x][y]: return False
    visited[x][y] = True

    for i in move:
        next_x = x + i[0]
        next_y = y + i[1]
        if in_scope(next_x, next_y) and not visited[next_x][next_y] and standard_arr[next_x][next_y] == standard_val:
            dfs(standard_arr, standard_val, next_x, next_y)
    return True

def solve(arr):
    count = 0
    for i in range(N):
        for j in range(N):
            
            if dfs(arr, arr[i][j], i, j):
                count += 1
    return count

if __name__ == "__main__":
    import sys
    sys.setrecursionlimit(int(10000))
    N = int(input())
    T = [[i for i in list(input())] for _ in range(N)]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]] 
    result = []

    # 일반
    visited = [[False for _ in range(N)] for _ in range(N)]
    result.append(solve(T))

    # RG 변환
    T = merge_rg(T)
    visited = [[False for _ in range(N)] for _ in range(N)]
    result.append(solve(T))

    print(*result)

"""
4
GGRR
RRGG
BBBB
RRGG
"""