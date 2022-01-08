# 브론즈4
# 손익분기점
A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    diff = C-B
    print(A // diff + 1)

"""
1000 70 170

3 2 1

2100000000 9 10

0 20 20

11 3 5
"""