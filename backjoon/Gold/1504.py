# 골드4 
# 특정한 최단 경로
# X
import sys
import heapq
N, E = map(int, sys.stdin.readline().split())
INF = int(1e9)

graph = {}
for i in range(E):
    # 입력값 받기
    p1, p2, v = map(int, sys.stdin.readline().split())
    # 그래프 그리기
    if graph.get(p1):
        graph.get(p1)[p2] = v
    else:
        graph[p1] = {p2 : v}

    if graph.get(p2):
        graph.get(p2)[p1] = v
    else:
        graph[p2] = {p1 : v}
v1, v2 = map(int, sys.stdin.readline().split())
q = []
# print(graph)

# 다익스트라 알고리즘
def dijkstra(start, end):
    # 비교값 저장
    distance = [INF] * (N+1)
    distance[start] = 0

    q = [(0, start)]

    while q:
        dist, now = heapq.heappop(q)
        for i in graph[now]:
            cost = dist + graph[now][i] # 현재까지의 이동 비용에서 다음 경로로 이동하는 비용 추가
            if cost < distance[i]: # 이전에 저장된 경로까지의 비용과 현재 이동 경로의 비용 중 최소 비용 비교
                distance[i] = cost
                heapq.heappush(q, (cost, i))
                # print(graph[now], i, graph[now][i], dist, now)

    # print("distance: ", distance)
    # print("end : ", distance[end])
    return distance[end]

path1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
path2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)
result = min(path1, path2)

if result >= INF:
    print(-1)
else:
    print(result)

"""
반례
4 6
1 2 3
2 3 3
3 4 1
1 3 5
2 4 5
1 4 4
2 3

4 2
1 2 3
3 4 4
2 3
"""