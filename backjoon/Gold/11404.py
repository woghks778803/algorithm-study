# 골드4
# 플로이드
# 다익스트라 알고리즘
def dijkstra(start):
    distance = [INF for _ in range(N+1)]
    distance[start] = 0
    q = [(0, start)]

    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = graph[now][i] + dist
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(q, (cost, i))

    for i in range(1, N+1):
        if distance[i] == INF: distance[i] = 0
    print(str(distance[1:]).replace(",","").replace("]","").replace("[",""))


if __name__ == "__main__":
    import sys, heapq
    from collections import defaultdict

    input = sys.stdin.readline
    INF = int(1e9)
    graph = defaultdict(dict)

    N = int(input()) # 도시 수
    M = int(input()) # 경로 갯수

    for _ in range(M):
        a, b, c = map(int, input().split())
        if graph.get(a):
            if graph.get(a).get(b):
                if graph.get(a).get(b) > c: graph[a][b] = c
            else:
                graph[a][b] = c
        else:
            graph[a] = {b : c}

    for i in range(1, N+1): dijkstra(i)

    # print(graph)
    # dijkstra(2)

"""
5
14
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
3 5 10
3 1 8
1 4 2
5 1 7
3 4 2
5 2 4

3
3
1 2 3
1 2 1
2 1 2

"""