# 실버4
# 코스튬 파티
import sys
input = sys.stdin.readline
N, S = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()
result = 0

for i in range(N):
    for j in range(i+1, N):
        if T[i]+T[j] <= S: result += 1
        else: break
        
print(result)

"""
4 6
3
5
2
1
"""