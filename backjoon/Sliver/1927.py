# 실버1
# 최소 힙
import sys
import heapq
N = int(sys.stdin.readline())
arr = []

for i in range(N):
    command = int(sys.stdin.readline())
    if command == 0:
        if arr: print(heapq.heappop(arr))
        else: print(0)
    else:
        heapq.heappush(arr, command)


"""
9
0
12345678
1
2
0
0
0
0
32
"""