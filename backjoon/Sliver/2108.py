# 실버4
# 통계학
import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
T = sorted([int(input()) for _ in range(N)])
counter = Counter(T)

result = []
max_num = max(counter.values())
for i in counter:
    if max_num == counter[i]: result.append(i)

print(round(sum(T)/N))
print(T[N//2])
if len(result) > 1:
    result.sort()
    print(result[1])
else: print(result[0])
print(max(T)-min(T))
"""
5
1
3
8
-2
2

3
0
0
-1
"""