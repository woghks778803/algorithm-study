# 골드4
# 집합의 표현
import sys
N, M = map(int, sys.stdin.readline().split())
p = {i : i for i in range(N+1)}
d = {i : 0 for i in range(N+1)}

def union(parent, child):
    x = find(parent)
    y = find(child)
    if x == y: return 

    if d[x] < d[y]: 
        # 부모보다 자식 뎁스가 높다면 그냥 부모를 아래로 두자 어차피 집합에만 넣으면됨
        p[x] = y
    else:
        p[y] = x

        if d[x] == d[y]: d[x] += 1

def check(parent, child):
    x = find(parent)
    y = find(child)

    if x == y: return True
    else: return False

def find(n):
    if p[n] == n: return n
    else: return find(p[n]) 

for i in range(M):
    c, a, b = map(int, sys.stdin.readline().split())

    if c == 0:
        union(a, b)
    else:
        result = check(a, b)
        if result: print("YES")
        else: print("NO")
    
    print(p)
    print(d)


"""
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""
