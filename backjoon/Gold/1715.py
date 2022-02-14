# 골드4
# 카드 정렬하기
# import random
import heapq
N = int(input())
T = []
result = 0
for _ in range(N):
    # heapq.heappush(T, random.randrange(1,11)) 
    heapq.heappush(T, int(input()))

while T:
    if len(T) < 2: break
    a = heapq.heappop(T)
    b = heapq.heappop(T)
    result += (a+b)
    T.append(a+b)

print(result)

"""
3
10
20
40
"""