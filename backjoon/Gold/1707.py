# 골드4
# 이분 그래프
import sys
from collections import defaultdict
from collections import deque
K = int(sys.stdin.readline())
TYPE1 = 1
TYPE2 = 2
TYPENONE = None
result = []

# bfs 알고리즘
def bfs(start):
    deq = deque()
    deq.append([start, TYPE2])

    while len(deq) > 0:
        
        visit_point, parent_type = deq.popleft()
        
        if visit_list[visit_point-1] == False:
            visit_list[visit_point-1] = True

            # 이전 노드 타입 값과 비교
            if parent_type == TYPE1:
                type_list[visit_point-1] = TYPE2
            elif parent_type == TYPE2:
                type_list[visit_point-1] = TYPE1

            for child_node in graph[visit_point]:
                if visit_list[child_node-1] == False:
                    deq.append([child_node, type_list[visit_point-1]])
        else:
            # 방문한 적이 있고 이전 노드와 타입이 같다면
            if type_list[visit_point-1] == parent_type:
                global no_check
                no_check = True
                break

for _ in range(K):
    V, E = map(int, sys.stdin.readline().split())
    visit_list = [False for _ in range(V)] # 방문 이력 저장
    type_list = [None for _ in range(V)] # 타입 저장
    graph = defaultdict(list)

    for i in range(E):
        a, b = map(int, sys.stdin.readline().split())
        # 정점간의 관계 그래프로 저장
        graph[a].append(b)
        graph[b].append(a)
    
    no_check = False
    for i in graph:
        if visit_list[i-1] == False: bfs(i)

    result.append(no_check)

for no in result:
    if no: print("NO")
    else: print("YES")


"""
2
3 2
1 3
2 3
4 4
1 2
2 3
3 4
4 2
YES
NO

1
7 6
1 2
1 3
2 4
2 5
3 6
3 7
YES

1
6 6
1 3
3 4
4 2
2 5
5 6
6 1
YES

1
7 6
1 2
2 3
3 5
3 4
4 6
6 7
YES

1
7 5
1 2
2 3
3 5
4 6
6 7
YES

1
1 1
1 1

1
3 1
2 3
YES

1
5 2
1 3
4 5
YES

1
5 4
1 2
3 4
4 5
3 5
NO
"""