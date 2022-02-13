# 실버3
# 늑대와 양
def bfs(x, y, result):
    if result[0] == 0 or checked[y][x]: return
    checked[y][x] = True

    for k in move_point:
        next_move_x = x+k[0]
        next_move_y = y+k[1]
        if 0 <= next_move_x < C and 0 <= next_move_y < R and checked[next_move_y][next_move_x] == False:
            if T[next_move_y][next_move_x] == 'W':
                checked[next_move_y][next_move_x] = True
                result[0] = 0
            elif T[next_move_y][next_move_x] == 'S':
                bfs(next_move_x, next_move_y, result)
            else:
                checked[next_move_y][next_move_x] = True
                T[next_move_y][next_move_x] = 'D'

if __name__ == "__main__":
    R, C = map(int, input().split())
    T = [[i for i in list(input())] for _ in range(R)]
    checked = [[False for _ in range(C)] for _ in range(R)]
    result = [1]
    move_point = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    for i in range(R):
        for j in range(C):
            if T[i][j] == 'S' and checked[i][j] == False:
                bfs(j, i, result)

    print(result[0])
    if result[0] == 1:
        for i in range(R): 
            for j in range(C): 
                print(T[i][j], end="")
            print()

"""
6 6
..S...
..S.W.
.S....
..W...
...W..
......

1 2
SW

5 5
.S...
...S.
S....
...S.
.S...
"""