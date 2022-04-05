# 실버2
# 특정 거리의 도시 찾기
def dijkstra(graph, start):
    distance = [int(1e9) for _ in range(N+1)]
    distance[start] = 0
    q = [[0, start]]

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: continue
        for i in graph[now]:
            cost = dist+1
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q, [cost, i])

    result = []
    for i in range(1, N+1):
        if distance[i] == K: result.append(i)
    return result

if __name__ == "__main__":
    import sys
    import heapq
    from collections import defaultdict
    input = sys.stdin.readline
    output = sys.stdout.write

    # 도시의 개수 N, 도로의 개수 M, 거리 정보 K, 출발 도시의 번호 X
    N, M, K, X = map(int, input().split())
    T = [[int(i) for i in input().split()] for _ in range(M)]
    graph = defaultdict(list)
    for item in T:
        s, e = map(int, item)

        if graph.get(s):
            graph[s].append(e)
        else:
            graph[s] = [e]
    
    result = []
    result = dijkstra(graph, X)

    if not result:
        print(-1)
    else:
        for i in result: output(str(i)+'\n')


"""
4 4 2 1
1 2
1 3
2 3
2 4

4 3 2 1
1 2
1 3
1 4

4 4 1 1
1 2
1 3
2 3
2 4

5 6 2 4
4 2
1 5
2 5
1 3
3 5
2 3

3 1 1 1
1 3
"""