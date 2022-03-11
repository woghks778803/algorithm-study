# 실버1
# 그대, 그머가 되어
def dijkstra(start, end):
    distance = [INF for _ in range(N+1)]
    distance[start] = 0
    q = [[0, start]]

    while q:
        dist, now = heapq.heappop(q)

        for next in graph[now]:
            cost = dist+1
            if cost < distance[next]:
                distance[next] = cost
                heapq.heappush(q, [cost, next])
    return distance[end]

def graph_setting(graph):
    for _ in range(M):
        p, c = map(int, input().split())

        if graph.get(p): graph[p].append(c)
        else: graph[p] = [c]

        if graph.get(c): graph[c].append(p)
        else: graph[c] = [p]

    return graph

if __name__ == "__main__":
    import sys
    import heapq
    from collections import defaultdict
    input = sys.stdin.readline
    INF = int(1e9)
    a, b = map(int, input().split())
    N, M = map(int, input().split())

    graph = defaultdict(list)
    graph = graph_setting(graph)

    result = dijkstra(a, b)
    if result == INF: print(-1)
    else: print(result)


"""
1 2
4 4
1 3
1 4
3 2
4 2

2 3
3 3
1 2
1 3
3 2

1 6
6 5
1 4
4 3
3 5
2 6
4 5
"""