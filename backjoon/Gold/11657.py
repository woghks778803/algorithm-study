# 골드4
# 타임머신

# 벨만포드 알고리즘
def belman_ford(start):
    distance = [INF for _ in range(N+1)]
    distance[start] = 0 # 1번부터 비교를 시작하므로 시작점은 초기화

    for i in range(1, N+1): # 모든 간선을 N번 반복
        for now in range(1, N+1):
            if distance[now] == INF : continue # 연결된 간선이 없으니 패스
            for city in graph[now]:
                if i < N: # 반복값이 N번미만일때
                    if distance[city[0]] > distance[now] + city[1]:
                        distance[city[0]] = distance[now] + city[1]
                else: # 이 경우 모든 반복을 끝냄
                    if distance[city[0]] > distance[now] + city[1]:
                        return False # 마지막까지 최솟값 갱신시 무한 루프이다

    return distance

if __name__ == "__main__":
    import sys
    from collections import defaultdict

    input = sys.stdin.readline
    graph = defaultdict(list)
    INF = int(1e9)
    N, M = map(int, input().split())

    for i in range(M):
        a, b, c = map(int, input().split())
        if graph.get(a):
            graph[a].append([b, c])
        else:
            graph[a] = [[b, c]]

    result = belman_ford(1)
    if result:
        for i in range(2, N+1):
            if result[i] == INF: sys.stdout.write("-1\n")
            else: sys.stdout.write(str(result[i])+"\n")
    else:
        sys.stdout.write("-1\n")

"""
3 4
1 2 4
1 3 3
2 3 -1
3 1 -2

3 4
1 2 4
1 3 3
2 3 -4
3 1 -2

3 2
1 2 4
1 2 3

3 2
1 2 3
1 2 4

2 1
1 2 -100
무한하지않음
= -100

2 2
1 2 -100
1 2 3
= -100

3 2
2 3 -2
3 2 -2
"""
