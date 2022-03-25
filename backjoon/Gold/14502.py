# 골드5
# 연구소 
def safe_find(temp_map):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if temp_map[i][j] == 0:
                cnt += 1

    return cnt

def point_find(virus_lst, space_lst):
    for i in range(N):
        for j in range(M):
            if T[i][j] == 2:
                virus_lst.append([i,j])
            elif T[i][j] == 0:
                space_lst.append([i,j])

def bfs(wall):
    # deepcopy보다 빠름
    temp_map = [item[:] for item in T]
    for wx, wy in wall: temp_map[wx][wy] = 1

    dq = deque(virus_lst)

    while dq:
        x, y = dq.popleft()

        for m in move:
            next_x = m[0]+x
            next_y = m[1]+y

            if N > next_x >= 0 and M > next_y >= 0:
                if temp_map[next_x][next_y] == 0:
                    temp_map[next_x][next_y] = 2
                    dq.append([next_x, next_y])

    return safe_find(temp_map)

if __name__ == "__main__":
    from collections import deque
    from itertools import combinations

    N, M = map(int, input().split())
    T = [[int(i) for i in input().split()] for _ in range(N)]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    # 바이러스 위치 저장, 벽 세우기 가능한 위치 저장
    virus_lst = []
    space_lst = []
    point_find(virus_lst, space_lst)

    result = 0
    # 임의의 겹치지않는 좌표 3개
    for wall in combinations(space_lst, 3):
        result = max(result, bfs(wall))

    print(result)

"""
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

8 8
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
2 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
"""