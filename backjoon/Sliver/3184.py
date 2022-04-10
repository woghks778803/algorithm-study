# 실버2
# 양
from collections import deque
def bfs(x, y, w, s):
    dq = deque([])
    dq.append([x, y])

    while dq:
        x, y = dq.popleft()

        for m in move:
            next_x = x + m[0]
            next_y = y + m[1]

            if R > next_x >= 0 and C > next_y >= 0 and not visited[next_x][next_y]:
                visited[next_x][next_y] = True
                if T[next_x][next_y] == "#": continue
                if T[next_x][next_y] == "v": w += 1
                elif T[next_x][next_y] == "o": s += 1

                dq.append([next_x, next_y])

    if w >= s: s = 0
    else: w = 0

    global wolf
    global sheep
    wolf += w
    sheep += s

if __name__ == "__main__":
    R, C = map(int, input().split())
    T = [[i for i in list(input())] for _ in range(R)]
    visited = [[False for _ in range(C)] for _ in range(R)]
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    wolf = 0
    sheep = 0

    for r in range(R):
        for c in range(C):
            if not visited[r][c]:
                place_wolf = 0
                place_sheep = 0
                visited[r][c] = True

                if T[r][c] == "#": continue
                if T[r][c] == "v": place_wolf += 1
                elif T[r][c] == "o": place_sheep += 1

                bfs(r, c, place_wolf, place_sheep)

    print(sheep, wolf)
    # print(visited)
    # print(T)

"""
6 6
...#..
.##v#.
#v.#.#
#.o#.#
.###.#
...###

8 8
.######.
#..o...#
#.####.#
#.#v.#.#
#.#.o#o#
#o.##..#
#.v..v.#
.######.

9 12
.###.#####..
#.oo#...#v#.
#..o#.#.#.#.
#..##o#...#.
#.#v#o###.#.
#..#v#....#.
#...v#v####.
.####.#vv.o#
.......####.
"""