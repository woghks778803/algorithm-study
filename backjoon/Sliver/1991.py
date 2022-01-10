# 실버1
# 트리 순회

# 전위 순회
def preOrder(cur):
    if cur == ".":
        return 0

    print(cur,end="")
    preOrder(graph[cur][0])
    preOrder(graph[cur][1])

# 중위 순회
def inOrder(cur):
    if cur == ".":
        return 0

    inOrder(graph[cur][0])
    print(cur,end="")
    inOrder(graph[cur][1])

# 후위 순회
def postOrder(cur):
    if cur == ".":
        return 0

    postOrder(graph[cur][0])
    postOrder(graph[cur][1])
    print(cur,end="")

if __name__ == "__main__":
    N = int(input())
    graph = {}

    for i in range(N):
        n, l, r = map(str, input().split())
        graph[n] = (l, r)

    ROOT = 'A'
    preOrder(ROOT)
    print()
    inOrder(ROOT)
    print()
    postOrder(ROOT)


"""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""