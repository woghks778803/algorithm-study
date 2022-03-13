# 실버3
# 문자열 집합
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
S = {input() for _ in range(N)}

result = 0
for _ in range(M):
    if input() in S:
        result += 1

print(result)
print(S)

"""
5 11
baekjoononlinejudge
startlink
codeplus
sundaycoding
codingsh
baekjoon
codeplus
codeminus
startlink
starlink
sundaycoding
codingsh
codinghs
sondaycoding
startrink
icerink
"""