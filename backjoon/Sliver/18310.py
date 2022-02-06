# 실버3
# 안테나
from collections import Counter
INF = int(1e11)
N = int(input()) # 4
T = [int(i) for i in input().split()]
counter = Counter(T)

count = 0
total = sum(T)
min_total_dist = INF
for i in range(1, 100001):
    total += count # 현재까지 탐색한 구간의 포함 위치 갯수를 거리에 더함
    total -= N-count # 현재까지 탐색한 구간에 포함되지않은 갯수 거리에서 뺌
    if min_total_dist > total: # 최솟값 갱신
        min_total_dist = total
        result_pos = i
    else:
        break

    count += counter[i]

print(result_pos)

# 방법2
import sys
n = int(sys.stdin.readline().rstrip()) #4
n_list = list(map(int,sys.stdin.readline().split())) # 5 1 7 9
n_list.sort()

print(n_list[(n-1)//2])
"""
4
5 1 7 9
"""