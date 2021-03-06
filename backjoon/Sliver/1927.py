# 실버1
# 최소 힙
import sys
import heapq
N = int(sys.stdin.readline())
arr = []

for i in range(N):
    command = int(sys.stdin.readline())
    if command == 0:
        if arr: sys.stdout.write(str(heapq.heappop(arr))+"\n")
        else: sys.stdout.write(str(0)+"\n")
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