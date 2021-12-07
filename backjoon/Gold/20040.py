# 골드4
# 사이클 게임
import sys
N, M = map(int, sys.stdin.readline().split())
test = [list(map(int,sys.stdin.readline().split())) for _ in range(M)]
line_check = False
parent = {i : i for i in range(N)}
rank = {i : 0 for i in range(N)}

# union-find 알고리즘
def union(p, c):
    x = find(p)
    y = find(c)
    if x == y : return False

    if rank[x] < rank[y]:
        parent[x] = y
    else:
        parent[y] = x
        if rank[x] == rank[y]: rank[x] += 1

    return True

def find(n):
    if parent[n] == n: return n
    else: return find(parent[n])

for i in range(M):
    b, s = test[i][0], test[i][1]

    if not union(b, s) :
        line_check = True
        print(i+1)
        break
        
if not line_check: print(0)

print(parent)
print(rank)
print(test)

"""
6 5
0 1
1 2
2 3
5 4
0 4

6 5
0 1
1 2
1 3
0 3
4 5
"""