# 실버3
# 이진 트리
def bfs(n):
    dq = deque()
    dq.append([n, n])
    result = {}

    while dq:
        dist, depth = dq.popleft()

        for i in graph[dist]:
            result[i] = depth+1
            dq.append([i ,depth+1])

    return result
    
if __name__ == "__main__":
    from collections import defaultdict, deque
    graph = defaultdict(list)
    N = int(input())
    
    for i in range(1, N+1):
        parent = int(input())
        graph[parent].append(i)

    result = bfs(-1)
    for i in range(1, N+1): print(result[i])
    # print(graph)

"""
7
-1
1
1
2
2
3
3
"""