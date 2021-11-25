# 실버5
# 단어 정렬
import sys
N = int(sys.stdin.readline())
T = [sys.stdin.readline().strip() for _ in range(N)]
T = list(set(T))
dict = {}

for i in T:
    if dict.get(len(i)): dict.get(len(i)).append(i)
    else: dict[len(i)] = [i]

for i in dict: dict[i].sort()

for i in range(1, 51):
    if dict.get(i):
        for j in dict[i]: sys.stdout.write(j+"\n")

"""
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
"""