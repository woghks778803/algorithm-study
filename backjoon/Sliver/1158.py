# 실버5
# 요세푸스 문제
from collections import deque
N, K = map(int, input().split())
dq = deque([i for i in range(1, N+1)])
result = []

cnt = 0
while dq:
    cnt += K-1
    cnt = cnt%len(dq)
    result.append(dq[cnt])
    dq.remove(dq[cnt])

print(str(result).replace('[','<').replace(']','>'))