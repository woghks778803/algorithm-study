# 실버1
# 절댓값 힙
import sys
import heapq
N = int(sys.stdin.readline())
arr = []

for i in range(N):
    command = int(sys.stdin.readline())
    if command == 0:
        if arr: 
            pop = heapq.heappop(arr)
            sys.stdout.write(str(pop[1])+"\n")
        else: 
            sys.stdout.write(str(0)+"\n")
    else:
        heapq.heappush(arr, (abs(command), command))

"""
18
1
-1
0
0
0
1
1
-1
-1
2
-2
0
0
0
0
0
0
0
"""