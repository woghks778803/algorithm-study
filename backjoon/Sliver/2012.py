# 실버3
# 등수 매기기
import sys
input = sys.stdin.readline
N = int(input())
T = [int(input()) for _ in range(N)]
T.sort()

result = 0
for i in range(1, N+1): result += abs(i-T[i-1])
print(result)

"""
5
1
5
3
1
2
"""