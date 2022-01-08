# 골드5
# 최단경로
import sys
import heapq
from collections import defaultdict

# 다익스트라 알고리즘
def dijkstra(start):
    INF = int(1e9)

    distance = [INF for _ in range(V+1)]
    distance[start] = 0
    q = [(0, start)]

    # bfs 알고리즘
    while q:
        dist, now = heapq.heappop(q)

        for i in graph[now]:
            cost = dist+graph[now][i]
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    for i in range(1, V+1):
        if distance[i] == INF:
            sys.stdout.write("INF\n")
        else:
            sys.stdout.write(str(distance[i])+"\n")


if __name__ == "__main__":
    V, E = map(int, sys.stdin.readline().split())
    start = int(input())

    # 그래프 그리기
    graph = defaultdict(dict)
    for _ in range(E):
        u, v, w = map(int, sys.stdin.readline().split())
        if graph.get(u):
            if graph.get(u).get(v):
                if graph[u][v] > w:
                    graph[u][v] = w
            else:
                graph[u][v] = w
        else:
            graph[u] = {v : w}

    dijkstra(start)

    print(graph)


"""
5 6
1
5 1 1
1 2 2
1 3 3
2 3 4
2 4 5
3 4 6

5 8
1
5 1 1
1 2 2
1 2 3
1 2 4
1 3 3
2 3 4
2 4 5
3 4 6

"""