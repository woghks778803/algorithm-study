# 실버1
# 포도주 시식
import sys
N = int(sys.stdin.readline().strip())
T = [int(sys.stdin.readline().strip()) for _ in range(N)]

DP = [[0 for _ in range(N)] for _ in range(2)]

for i in range(N):
    if i == 0:
        DP[0][i] = T[i]
        DP[1][i] = T[i]
    elif i-2 < 0:
        DP[0][i] = T[i] + DP[1][i-1]
        DP[1][i] = T[i]
    else:
        DP[0][i] = T[i] + DP[1][i-1]
        DP[1][i] = T[i] + max(max(DP[0][:i-1]), max(DP[1][:i-1]))

print(max(max(DP[0]), max(DP[1])))

"""
6
6
10
13
9
8
1
=33

6
1
3
7
10
13
14
=37

7
1
5
3
7
10
13
1
=31

3
3
2
1
=5

6
1000 
1000
1
1
1000
1000
=4000
"""