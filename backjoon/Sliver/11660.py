# 실버1
# 구간 합 구하기 5
import sys
N, M = map(int, sys.stdin.readline().split())
T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

DP = [[0 for _ in range(N)] for _ in range(N)]
result = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    incre_num = 0
    for j in range(N):
        incre_num += T[i][j]
        DP[i][j] += incre_num

for i in range(N):
    for j in range(N):
        result[i][j] += T[i][j]
        if i>0: result[i][j] += result[i-1][j]
        if j>0: result[i][j] += DP[i][j-1]

def minus1(n): return int(n)-1

for _ in range(M):
    x1, y1, x2, y2 = map(minus1, sys.stdin.readline().split())

    if x1 == 0 and y1 == 0:
        sys.stdout.write(str(result[x2][y2])+'\n')
    elif x1 == 0:
        sys.stdout.write(str(result[x2][y2] - result[x2][y1-1])+'\n')
    elif y1 == 0:
        sys.stdout.write(str(result[x2][y2] - result[x1-1][y2])+'\n')
    else:
        sys.stdout.write(str(result[x2][y2] + result[x1-1][y1-1] - result[x1-1][y2] - result[x2][y1-1])+'\n')


"""
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4

2 4
1 2
3 4
1 1 1 1
1 2 1 2
2 1 2 1
2 2 2 2

3 1
2 4 1
2 5 2
2 6 4
"""