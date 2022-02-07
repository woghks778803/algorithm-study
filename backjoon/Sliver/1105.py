# 실버1
# 팔
from collections import deque
L, R = map(deque, input().split())

if len(R)>len(L):
    print(0)
else:
    cnt = 0
    for _ in range(len(R)):
        if L[0] == R[0]:
            if L[0] == '8': cnt += 1
            L.popleft()
            R.popleft()
    
    print(cnt)

"""
800 899
8808 8880
88 88000
9999 9999
5888 5888
"""