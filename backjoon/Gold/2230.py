# 골드5
# 수 고르기
import sys
input = sys.stdin.readline
INF = int(2e9)
N, M = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()

# 투 포인터
result = INF
start = 0
end = 1
while start < N and end < N:
    diff = T[end] - T[start]
    if T[end] - T[start] >= M:
        result = min(diff, result)
        start += 1
    else:
        end += 1

print(result)

# print(T)

"""
3 3
1
5
3

3 1
1
2
3
"""