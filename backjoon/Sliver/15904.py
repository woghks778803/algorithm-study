# 실버5
# UCPC는 무엇의 약자일까?
from collections import deque 
s = list(input())
UCPC = deque(list("UCPC"))
check_str = UCPC.popleft()

for i in s:
    if check_str == i:
        if UCPC:
            check_str = UCPC.popleft()
        else:
            check_str = None
            break

if check_str: print("I hate UCPC")
else: print("I love UCPC")

# print(check_str)


"""
Union of Computer Programming Contest club contest
"""