# 실버4
# 카드2
import collections
N = int(input())

T = [i for i in range(1, N+1)]
deq = collections.deque(T)

while True:
    throw_deq = deq.popleft()
    if not deq: 
        print(throw_deq) 
        break
    append_deq = deq.popleft()
    deq.append(append_deq)
