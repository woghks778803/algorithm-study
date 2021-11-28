# 실버4
# 숫자 카드 2
# 1번
N = int(input())
T_N = list(map(int, input().split()))
M = int(input())
T_M = list(map(int, input().split()))
dict = {k : 0 for k in T_M}

for i in T_N:
    if i in dict.keys(): dict[i] += 1

for i in T_M: print(dict[i], end=" ")

# 2번
N = int(input())
T_N = list(map(int, input().split()))
set_T_N = set(T_N)
M = int(input())
T_M = list(map(int, input().split()))

dict = {}
for i in set_T_N: dict[i] = T_N.count(i)

for i in T_M:
    if dict.get(i): print(dict[i], end=" ")
    else: print(0, end=" ")
"""
10
6 3 2 10 10 10 -10 -10 7 3
9
10 10 9 -5 2 3 4 5 -10

10
6 3 2 10 10 10 -10 -10 7 3
8
10 9 -5 2 3 4 5 -10
"""