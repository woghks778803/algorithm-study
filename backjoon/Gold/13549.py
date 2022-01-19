# 골드5
# 숨바꼭질 3
def dijkstra(start, end):
    distances = [float('inf')] * 200001
    distances[start] = 0
    q = [(distances[start], start)]

    while q:
        cnt, point = heapq.heappop(q)

        if point == end:
            return cnt

        for i in range(len(tp)):
            if tp[i] == PLUS:
                next_point = point+1
                next_cnt = cnt+1
            elif tp[i] == MINUS:
                next_point = point-1
                next_cnt = cnt+1
            elif tp[i] == MULTI:
                next_point = point*2
                next_cnt = cnt

            if 0 <= next_point <= 100000 and cnt < distances[next_point]:
                distances[next_point] = next_cnt
                heapq.heappush(q, [distances[next_point], next_point])


if __name__ == "__main__":
    import heapq
    N, M = map(int, input().split())

    PLUS = "+1"
    MINUS = "-1"
    MULTI = "x2"
    tp = [PLUS, MINUS, MULTI]

    print(dijkstra(N, M))
    
"""
5 17
"""