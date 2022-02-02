# 실버2
# 촌수계산
def find(node, parent, cnt):
    if graph[node] == node:
        return node
    else:
        cnt += 1
        parent.append([graph[node], cnt])
        return find(graph[node], parent, cnt)

if __name__ == "__main__":
    N = int(input())
    a, b = map(int, input().split())
    M = int(input())
    graph = {}
    a_parent = []
    a_parent.append([a, 0])
    b_parent = []
    b_parent.append([b, 0])

    for _ in range(M):
        x,y = map(int, input().split())
        graph[y] = x

        if graph.get(x): pass
        else: graph[x] = x

    if find(a, a_parent, 0) == find(b, b_parent, 0):
        result = 0
        while True:
            if a_parent: a_pop = a_parent.pop()
            else: break

            if b_parent: b_pop = b_parent.pop()
            else: break

            if a_pop[0] == b_pop[0]: result = a_pop[1] + b_pop[1]
            else: break
        
        print(result)
    else:
        print(-1)
        



"""
9
7 3
7
1 2
1 3
2 7
2 8
2 9
4 5
4 6

"""