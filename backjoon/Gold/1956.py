# 골드4
# 운동
# 다익스트라 알고리즘
def dijkstra(point):
    distance = [INF for _ in range(V+1)]
    q = [(0, point)]

    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = i[1] + dist
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return distance[point]
    # print(distance)

if __name__ == "__main__":
    import heapq
    from collections import defaultdict

    V, E = map(int, input().split())
    INF = int(1e9)
    graph = defaultdict(list)
    ans = []

    for i in range(E):
        a, b, c = map(int, input().split())
        
        if graph.get(a): graph[a].append([b,c])
        else: graph[a] = [[b,c]]

    for i in range(1, V+1): ans.append(dijkstra(i))
    
    if min(ans) == INF: print(-1)
    else: print(min(ans))
"""
3 4
1 2 1
3 2 1
1 3 5
2 3 2

3 6
1 2 1
3 2 1
1 3 5
2 1 3
2 3 2
3 1 1
"""    
