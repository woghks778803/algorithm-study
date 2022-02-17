# 실버5
# 소가 길을 건너간 이유 1
from collections import deque
N = int(input())
T = deque([[int(i) for i in input().split()] for _ in range(N)])
looking_data = {}

result = 0
while T:
    cow = T.popleft()
    if looking_data.get(cow[0]) is not None and looking_data[cow[0]] != cow[1]:
        result += 1
    looking_data[cow[0]] = cow[1]
print(result)

"""
8
3 1
3 0
6 0
2 1
4 1
3 0
4 0
3 1
"""

