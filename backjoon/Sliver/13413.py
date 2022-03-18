# 실버4
# 오셀로 재배치
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    N = int(input())
    T = input()
    R = input()
    diff = {"W" : 0, "B" : 0}
    for i in range(N):
        if R[i] != T[i]: diff[T[i]] += 1

    if diff["B"] < diff["W"]: print(diff["W"])
    else: print(diff["B"])





"""
3
5
WBBWW
WBWBW
7
BBBBBBB
BWBWBWB
4
WWBB
BBWB
"""