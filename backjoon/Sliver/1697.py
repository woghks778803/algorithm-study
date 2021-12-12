# 실버1
# 숨바꼭질 
from collections import deque
N, K = map(int, input().split())
INF = 100000
visit = [False for _ in range(INF+1)]
depth = [0 for _ in range(INF+1)]
move_point = [-1, 1, 2]

def bfs():
    loop_check = False
    deq = deque()
    deq.append(N)
    visit[N] = True

    while len(deq) > 0:
        point = deq.popleft()
        for i in range(len(move_point)): 
            if i == 2: next_point = point*move_point[i]
            else: next_point = point+move_point[i]

            if INF >= next_point >= 0 and visit[next_point] == False:
                depth[next_point] = depth[point]+1
                visit[next_point] = True
                deq.append(next_point)
                if next_point == K:
                    loop_check = True
                    break
        
        if loop_check: break

bfs()
print(depth[K])

"""
5 17
= 4

3482 45592
= 637
"""