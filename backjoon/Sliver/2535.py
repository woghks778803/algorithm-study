# 실버5
# 아시아 정보올림피아드
N = int(input())
T = [[int(i) for i in input().split()] for _ in range(N)]
T.sort(key= lambda x : -x[2])
LIMIT = 2
medal = 3
graph = {}

for i in T:
    if graph.get(i[0]): graph[i[0]] += 1
    else: graph[i[0]] = 1
        
    if graph[i[0]] <= 2 and medal > 0:
        medal -= 1
        print(i[0], i[1])

# print(T)
# print(graph)

"""
9
1 1 230
1 2 210
1 3 205
2 1 100
2 2 150
3 1 175
3 2 190
3 3 180
3 4 195
"""