# 실버1
# 전깃줄
# X
import sys
N = int(sys.stdin.readline())
T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
T = sorted(T)
DP = [1 for _ in range(501)]
line = {}

for i in T:
    line[i[0]] = i[1]

for i in line:
    for j in line:
        if j < i and line[j] < line[i]:
            DP[i] = max(DP[i], DP[j]+1) 

print(N-max(DP))
"""
8
1 8
3 9
2 2
4 1
6 4
10 10
9 7
7 6
=3

10
1 6
2 8
3 2
4 9
5 5
6 10
7 4
8 1
9 7
10 3
=6

4
1 8
3 2
4 3
5 4

4
1 8
2 3
4 5
3 4
"""