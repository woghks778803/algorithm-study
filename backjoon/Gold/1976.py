# 골드4
# 여행 가자
import sys
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
n_city = {i : i for i in range(N)}
n_map = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
move_list = list(map(int, sys.stdin.readline().split()))

# union-find 알고리즘
def union(root, child):
    r = find(root)
    c = find(child)

    if r == c : return
    n_city[c] = r

def find(n):
    if n_city[n] != n: 
        n_city[n] = find(n_city[n])
    return n_city[n]

for i in range(N): 
    for j in range(i+1, N):
        if n_map[i][j] == 1: union(i, j)

ans = set([find(n_city[i-1]) for i in move_list])
if len(ans) == 1:
    print("YES")
else:
    print("NO")

print(ans)
print(n_map)
print(move_list)
print(n_city)

"""
3
3
0 1 0
1 0 1
0 1 0
1 2 3
= YES

3
2
0 1 0
1 0 1
0 1 0
1 1
= YES

6
6
0 1 0 0 1 0
1 0 1 0 0 0
0 1 0 1 0 0
0 0 1 0 0 0
1 0 0 0 0 1
0 0 0 0 1 0
1 2 3 4 5 6
= YES

6
6
0 1 0 0 0 0
1 0 1 0 0 1
0 1 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 1
0 1 0 0 1 0
1 2 3 4 5 6
= YES

6
6
0 1 0 0 0 0
1 0 1 0 0 1
0 1 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 1
0 1 0 0 1 0
3 2 4 5 1 6 2
= YES

6
6
0 1 0 0 0 0
1 0 1 0 0 0
0 1 0 0 0 0
0 0 0 0 1 0  
0 0 0 1 0 1  
0 0 0 0 1 1  
3 2 4 5 1 6 2
= NO

6
6
0 1 0 0 0 0
1 0 1 0 0 0
0 1 0 0 0 0
0 0 0 0 1 0
0 0 0 1 0 1
0 0 0 0 1 0
1 2 3 4 5 6
= NO

5
5
0 1 0 1 1
1 0 1 1 0
0 1 0 0 0
1 1 0 0 0
1 0 0 0 0
5 3 2 3 4
= YES

8
8
0 1 0 0 0 0 0 0 
1 0 1 1 0 0 0 0
0 1 0 0 0 1 0 0
0 1 0 0 1 0 0 0
0 0 0 1 0 0 1 1
0 0 1 0 0 0 0 0
0 0 0 0 1 0 0 0
0 0 0 0 1 0 0 0
1 4 6 5 2 4 3 4 1 2 8 6 7
= YES

4
4
0 0 0 1
0 0 1 0
0 1 0 1
1 0 1 0
3 1 2 4
= YES

5
3
0 0 0 1 0
0 0 1 0 0
0 1 0 1 0
1 0 1 0 0
0 0 0 0 0
1 2 3
= YES

5
2
0 1 1 0 0
1 0 0 0 0
1 0 0 0 0
0 0 0 0 1
0 0 0 1 0
4 5
= YES
"""