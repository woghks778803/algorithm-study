# 골드5
# Fly me to the Alpha Centauri
# X
import sys
import math
T = int(sys.stdin.readline().strip())

def calc(move, end):
    r = end-move
    count = 0
    math_sqrt = math.sqrt(r)
    round_math_sqrt = round(math_sqrt)
    rr = math_sqrt % 1
    if round_math_sqrt > math_sqrt or rr == 0:
        count = round_math_sqrt + round_math_sqrt-1
    else:
        count = round_math_sqrt + round_math_sqrt
    print(count)

for i in range(T):
    X, Y = map(int, sys.stdin.readline().split())
    calc(X, Y)



"""
반례 
3
0 3
1 5
45 50

1
0 1
= 1

1
0 2
= 2

1
0 3
= 3

1
0 4
= 3
"""