# 실버3
# 파일 정리
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())
    graph = {}
    for _ in range(N):
        name, extension = input().strip().split('.')

        if graph.get(extension): graph[extension] += 1
        else:graph[extension] = 1
    sorted_graph = sorted(graph.items())
    for i in sorted_graph: print(i[0], i[1])


"""
8
sbrus.txt
spc.spc
acm.icpc
korea.icpc
sample.txt
hello.world
sogang.spc
example.txt
"""