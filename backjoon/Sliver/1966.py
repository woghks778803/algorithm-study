# 실버3
# 프린터 큐
import sys
import collections
T = int(sys.stdin.readline())

for i in range(T):
    N, M = map(int, sys.stdin.readline().split())
    I = collections.deque(list(map(int, sys.stdin.readline().split())))
    temp = collections.deque([i for i in range(N)])

    count = 0
    while True:
        if max(I) == I[0]:
            count += 1
            i_pop = I.popleft()
            temp_pop = temp.popleft()

            if temp_pop == M: break
        else:
            i_pop = I.popleft()
            I.append(i_pop)
            temp_pop = temp.popleft()
            temp.append(temp_pop)

    print(count) 

"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
"""