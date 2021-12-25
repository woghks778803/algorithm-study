# 실버3
# 구간 합 구하기 4
import sys
N, M = map(int, sys.stdin.readline().split())
T = list(map(int, sys.stdin.readline().split()))
DP = [0 for _ in range(N)]
incre_num = 0

for i in range(N): 
    incre_num += T[i]
    DP[i] += incre_num

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    if i-2 >= 0: sys.stdout.write(str(DP[j-1] - DP[i-2])+"\n")
    else: sys.stdout.write(str(DP[j-1])+"\n")
# print(DP)

"""
5 3
5 4 3 2 1
1 3
2 4
5 5
"""