# 실버3
# 삼각형 만들기
import sys
input = sys.stdin.readline
N = int(input())
T = [int(input()) for _ in range(N)]
T.sort()

result = -1
for i in range(N-1, 1, -1):
    if T[i] < T[i-1] + T[i-2]:
        result = T[i-2] + T[i-1] + T[i]
        break
print(result)

"""
3
1
2
3
"""