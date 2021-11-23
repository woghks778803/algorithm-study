# 실버4
# 요세푸스 문제 0
import collections
N, K = map(int, input().split())
T = [i for i in range(1, N+1)]
deq = collections.deque(T)
result = []

for i in range(N):
    for j in range(1, K+1):
        temp = deq.popleft()
        if j < K: deq.append(temp)
        else: result.append(temp)

result_str = "<"
for i in range(len(result)):
    if result[i] == result[-1]: result_str += str(result[i])+">"
    else: result_str += str(result[i])+", "
print(result_str)



"""
7 3
"""