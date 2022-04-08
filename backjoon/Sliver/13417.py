# 실버3
# 카드 문자열
from collections import deque

T = int(input())
for i in range(T):
    n = int(input())
    arr = [i for i in input().split()]
    dq = deque([arr[0]])

    for a in arr[1:]:
        if a <= dq[0]:
            dq.appendleft(a)
        else:
            dq.append(a)
    
    print("".join(dq))

        


"""
3
3
M K U
5
A S D F G
7
B A C A B A C
"""