# 실버4
# 회전하는 큐
import collections
N, M = map(int, input().split())
T = list(map(int, input().split()))
deq = collections.deque([i for i in range(1, N+1)])
result = 0

for i in T:
    if len(deq) - deq.index(i) > deq.index(i):
        result += deq.index(i)
        for j in range(deq.index(i)):
            deq.append(deq.popleft())
    else:
        result += len(deq) - deq.index(i)
        for j in range(len(deq) - deq.index(i)):
            deq.appendleft(deq.pop())
    deq.popleft()
print(result)



"""
10 3
1 2 3

10 3
2 9 5

32 6
27 16 30 11 6 23

10 10
1 6 3 2 7 9 8 4 10 5
"""