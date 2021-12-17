# 실버4
# 상근이의 여행
from collections import defaultdict 
import sys

# bfs 알고리즘
def bfs(cur_point, country_check, count):
    for i in graph[cur_point]:
        if country_check[i-1] == False:
            country_check[i-1] = True
            count += 1
            bfs(i, country_check, count)

            if country_check.count(True) == N:
                result.append(count)
                return

T = int(sys.stdin.readline())
result = []
for _ in range(T):
    N, M = map(int, sys.stdin.readline().strip().split())
    result = []
    graph = defaultdict(list)

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().strip().split())
        graph[a].append(b)
        graph[b].append(a)

    # for i in graph:
    #     for j in graph[i]:
    #         count = 1
    #         country_check = [False for _ in range(N)]
    #         country_check[i-1] = True
    #         country_check[j-1] = True
    #         bfs(j, country_check, count)

    sys.stdout.write(str(N-1)+"\n")

"""
2
3 3
1 2
2 3
1 3
5 4
2 1
2 3
4 3
4 5

1
2 1
1 2

1
3 3
1 2
2 3
1 3

1
6 5
1 2
2 3
3 4
4 5
4 6

1
6 6
1 2
2 3
3 6
3 4
4 5
4 6

1
7 6
1 2
1 3
1 4
1 5
1 6
1 7

1
7 7
1 2
1 3
1 4
1 5
1 6
1 7
2 7
"""