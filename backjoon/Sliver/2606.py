# 실버3
# 바이러스
C_N = int(input())
L_N = int(input())
C = {i : i for i in range(1, C_N+1)}

def union(root, child):
    x = find(root)
    y = find(child)
    if x == y : return
    C[y] = x

def find(n):
    if C[n] == n: return n
    else: return find(C[n])

for i in range(L_N):
    a, b = map(int, input().split())
    union(a, b)

result = 0
for i in C:
    if find(C[1]) == find(C[i]): result += 1

print(result-1)

"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7

3
1
2 3

3
1
2 1

7
6
2 3
1 5
5 2
5 6
1 2
4 7

9
9
1 2
1 3
1 4
3 8
3 9
4 5
4 6
6 8
6 7
"""