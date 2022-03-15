# 플레티넘5
# 백조와 호수
from collections import deque
import sys

input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    while q:
        x, y = q.popleft()
        if x == x2 and y == y2:
            return 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not c[nx][ny]:
                    if a[nx][ny] == '.':
                        q.append([nx, ny])
                    else:
                        q_temp.append([nx, ny])
                    c[nx][ny] = 1
    return 0

def melt():
    while wq:
        x, y = wq.popleft()
        if a[x][y] == 'X':
            a[x][y] = '.'
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if not wc[nx][ny]:
                    if a[nx][ny] == 'X':
                        wq_temp.append([nx, ny])
                    else:
                        wq.append([nx, ny])
                    wc[nx][ny] = 1

m, n = map(int, input().split())
c = [[0]*n for _ in range(m)]
wc = [[0]*n for _ in range(m)]

a, swan = [], []
q, q_temp, wq, wq_temp = deque(), deque(), deque(), deque()

for i in range(m):
    row = list(input().strip())
    a.append(row)
    for j, k in enumerate(row):
        if a[i][j] == 'L':
            swan.extend([i, j])
            wq.append([i, j])
        elif a[i][j] == '.':
            wc[i][j] = 1
            wq.append([i, j])

x1, y1, x2, y2 = swan
q.append([x1, y1])
a[x1][y1], a[x2][y2], c[x1][y1] = '.', '.', 1
cnt = 0

while True:
    melt()
    if bfs():
        print(cnt)
        break
    q, wq = q_temp, wq_temp
    q_temp, wq_temp = deque(), deque()
    cnt += 1

# 방법2
def in_lake(x, y):
    if 0 <= x < R and 0 <= y < C: return True
    else: return False

def find(n):
    if graph[n] != n:
        graph[n] = find(graph[n])

    return graph[n]

def union(parent, child):
    r = find(parent)
    n = find(child)

    if r == n : return 

    graph[n] = r

def union_check(parent, child):
    r = find(parent)
    n = find(child)

    if r == n : return True
    else: return False

def merge(merge_q):
    dq = deque(merge_q)

    while dq:
        x, y = dq.popleft() 
        melt_q.append([x, y])

        for i in move:
            next_x = x+i[0]
            next_y = y+i[1]

            if in_lake(next_x, next_y) and merge_visited[next_x][next_y] and x*C+y >= 0 and x*C+y != next_x*C+next_y:
                union(x*C+y, next_x*C+next_y)

def melt(melt_q):
    dq = deque(melt_q)

    while dq:
        x, y = dq.popleft()

        for i in move:
            next_x = x+i[0]
            next_y = y+i[1]

            if in_lake(next_x, next_y) and not merge_visited[next_x][next_y]:
                merge_visited[next_x][next_y] = True
                merge_q.append([next_x, next_y])

  
if __name__ == "__main__":
    import sys
    from collections import deque
    input = sys.stdin.readline

    R, C = map(int, input().split())
    T = [list(input().strip()) for _ in range(R)]
    
    move = [[0,1],[0,-1],[1,0],[-1,0]]
    merge_visited = [[False for _ in range(C)] for _ in range(R)]
    graph = {i:i for i in range(R*C)}
    swan = []
    merge_q = []
    melt_q = []

    # 백조 좌표 먼저 저장
    for i in range(R):
        for j in range(C):
            if T[i][j] == 'L': swan.append([i, j, i*C+j]) # 체크용 백조 위치 저장
            if T[i][j] != 'X': 
                merge_visited[i][j] = True
                merge_q.append([i, j])

    ans = 0
    while True:
        # 백조 주변 물 병합
        merge(merge_q)

        union_result = union_check(swan[0][2], swan[1][2])
        if union_result: 
            print(ans)
            break
        
        # 백조 위치의 물 유니온 파인드
        melt(melt_q)
        ans += 1

    

"""
10 2
.L
..
XX
XX
XX
XX
XX
XX
..
.L

4 11
..XXX...X..
.X.XXX...L.
....XXX..X.
X.L..XXX...

8 17
...XXXXXX..XX.XXX
....XXXXXXXXX.XXX
...XXXXXXXXXXXX..
..XXXXX.LXXXXXX..
.XXXXXX..XXXXXX..
XXXXXXX...XXXX...
..XXXXX...XXX....
....XXXXX.XXXL...

5 7
..XXXX.
XX.LXXX
.X..XXX
..XXXX.
...X..L

"""