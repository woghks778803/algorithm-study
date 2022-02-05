# 실버1
# 효율적인 해킹
def bfs(temp, first):
    visited = [False for _ in range(N+1)]
    dq = deque([first])
    visited[first] = True

    while dq:
        next = dq.popleft()
        temp.append(next)
        
        for i in graph[next]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)

    return temp

if __name__ == "__main__":
    import sys
    from collections import deque
    from collections import defaultdict
    input = sys.stdin.readline
    output = sys.stdout.write
    N, M = map(int, input().split())
    graph = defaultdict(list)

    for _ in range(M):
        A, B = map(int, input().split())
        graph[B].append(A)
    
    result = list()
    maxNum = 0
    for i in range(1, N+1):
        temp = bfs([], i)
        temp_cnt = len(temp)

        if temp_cnt > maxNum:
            result = list()
            maxNum = temp_cnt
            result.append(i)
        elif temp_cnt == maxNum:
            result.append(i)

    for i in result: output(str(i)+" ")

    # print(graph)
    # print(result)

"""
5 4
3 1
3 2
4 3
5 3

2 2
1 2
2 1
"""