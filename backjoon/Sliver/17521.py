# 실버5
# Byte Coin
import sys
input = sys.stdin.readline
N, W = map(int, input().split())
T = [int(input()) for _ in range(N)]
UP, DOWN = 1, -1

coin = 0
position_toggle = None

for i in range(N):
    if i == N-1:
        if coin != 0:
            W += T[N-1]*coin
            coin = 0
    else:
        if T[i] > T[i+1]:
            if position_toggle != DOWN:
                W += T[i]*coin
                coin = 0
            position_toggle = DOWN
        elif T[i] < T[i+1]:
            if position_toggle != UP:
                coin = W//T[i]
                W -= T[i]*coin
            position_toggle = UP

print(W)

"""
10 24
5
7
5
4
2
7
8
5
3
4

5 15
5
4
4
2
7

7 54
7
5
5
4
2
2
1
"""