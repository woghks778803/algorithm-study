# 골드4
# 단어 수학
N = int(input())
T = [list(input()) for _ in range(N)]
graph = {}

for t in T:
    len_t = len(t)
    for j in range(len_t):
        if graph.get(t[j]):
            graph[t[j]] += 10**(len_t-j)
        else:
            graph[t[j]] = 10**(len_t-j)

lst = list(graph.items())
lst.sort(key= lambda x : -x[1])

result = 0
for i in range(9, 9-len(lst), -1):
    result += lst[9-i][1]*i

print(result//10)
# 9865
# 9787
# 19652
"""
2
GCF
ACDEB

2
AB
BA

2
DABG
DCAC
"""