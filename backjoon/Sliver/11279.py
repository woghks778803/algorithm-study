# 실버2
# 최대 힙
import sys
import heapq
N = int(sys.stdin.readline())
arr = []

for i in range(N):
    command = int(sys.stdin.readline())
    if command == 0:
        if arr: sys.stdout.write(str(abs(heapq.heappop(arr)))+"\n")
        else: sys.stdout.write(str(0)+"\n")
    else:
        heapq.heappush(arr, -command)
        

"""
13
0
1
2
0
0
3
2
1
0
0
0
0
0
"""