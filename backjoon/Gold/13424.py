# 골드4
# 비밀 모임
from collections import defaultdict
import heapq
import sys

def dijkstra(start):
    distance = [INF for _ in range(N+1)]
    distance[start] = 0
    q = [[0, start]]

    while q:
        dist, now = heapq.heappop(q)

        for g in graph[now]:
            cost = dist+g[1]
            if distance[g[0]] > cost:
                distance[g[0]] = cost
                heapq.heappush(q, [distance[g[0]], g[0]])

    return distance

if __name__ == "__main__":
    input = sys.stdin.readline
    T = int(input())
    INF = int(1e9)

    for i in range(T):
        N, M = map(int, input().split())

        graph = defaultdict(list)
        for i in range(M):
            a, b, c = map(int, input().split())
            graph[a].append([b, c])
            graph[b].append([a, c])

        K = int(input())
        friends = [int(i) for i in input().split()]

        min_cost = INF
        result = 0
        for r in range(1, N+1):
            distance = dijkstra(r)

            cost = 0
            for f in friends:
                cost += distance[f]
            
            if min_cost > cost:
                min_cost = cost
                result = r

        print(result)

"""
2
6 7
1 2 4
1 3 1
1 5 2
2 3 2
3 4 3
4 5 2
6 5 1
2
3 5
4 5
1 2 2
1 3 1
2 3 2
2 4 3
3 4 6
2
3 4
"""