# 실버3
# 피보나치 수열
import sys
import heapq
N = int(sys.stdin.readline())

def fibonacci_calc(n):
    heap_list = [(1, 0), (0, 1)]
    if n == 0:
        print(1, 0)
    elif n == 1:
        print(0, 1)
    else:
        for i in range(2, n+1):

            la, lb = heapq.heappop(heap_list)
            ra, rb = heapq.heappop(heap_list)
            t_la = la
            t_lb = lb
            la = ra
            lb = rb
            ra = t_la+ra
            rb = t_lb+rb

            heapq.heappush(heap_list, (la, lb))
            heapq.heappush(heap_list, (ra, rb))
            
            if i == n:
                print(ra, rb)

for i in range(N):
    T = int(sys.stdin.readline())
    fibonacci_calc(T)



"""
반례 
3
0
1
3

2
6
22

2
1
40

"""