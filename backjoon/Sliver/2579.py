# 실버3
# 계단 오르기
import sys
N = int(sys.stdin.readline())

N_LIST = [int(sys.stdin.readline()) for i in range(N)]
CHECK_LIST = [[0, 0] for i in range(N)]

if N == 1:
    print(N_LIST[0])
elif N == 2:
    print(N_LIST[0]+N_LIST[1])
else:
    CHECK_LIST[0][0] = N_LIST[0]
    index = 1
    while True:
        if index - 2 >= 0:
            CHECK_LIST[index][0] = N_LIST[index] + max(CHECK_LIST[index-2][0], CHECK_LIST[index-2][1])
        else:
            CHECK_LIST[index][0] = N_LIST[index]
        CHECK_LIST[index][1] = N_LIST[index] + CHECK_LIST[index-1][0]
        index += 1
        if N <= index:
            break
    print(max(CHECK_LIST[N-1][0], CHECK_LIST[N-1][1]))


"""
6
10
20
15
25
10
20
=75

12
10
22
23
25
10
15
11
10
23
21
15
14
=142
"""