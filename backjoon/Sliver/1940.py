# 실버4
# 주몽
if __name__ == "__main__":
    N = int(input())
    M = int(input())
    T = [int(i) for i in input().split()]

    graph = {}
    result = 0
    for i in T:
        if graph.get(i): result += 1
        else: graph[M-i] = True

    print(result)
    print(graph)

"""
6
9
2 7 4 1 5 3
"""