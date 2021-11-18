# 골드5
# 평범한 배낭
import sys
N, K = map(int, sys.stdin.readline().split())

memo_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
DP = [0 for _ in range(K+1)]

# DP
for i in range(N):
    for j in reversed(range(memo_list[i][0], K+1)):
        DP[j] = max(DP[j], DP[j-memo_list[i][0]]+memo_list[i][1])

print(max(DP))

# DFS
# def recursion(index, w, sum_n):
#     for i in reversed(range(index+1, N)):
#         weight = w + memo_list[i][0]
#         sum_num = sum_n + memo_list[i][1]
#         if weight <= K:
#             DP[weight] = max(DP[weight], sum_num)

#             recursion(i, weight, sum_num)

# for i in range(N):
#     if memo_list[i][0] <= K:
#         DP[memo_list[i][0]] = max(DP[memo_list[i][0]], memo_list[i][1])
#         recursion(i, memo_list[i][0], memo_list[i][1])

# print(max(DP))
"""
반례

14 100000
61803 5
62863 0
41632 3
12794 2
71324 8
55358 2
34870 8
41590 7
17928 0
24218 3
18426 0
65130 2
16478 2
93173 9
= 17

4 8
6 13
4 8
4 6
5 12
=14

10 999
46 306
60 311
33 724
18 342
57 431
49 288
12 686
89 389
82 889
16 289
=4655

3 5
4 2
3 4
1 5
=9

6 25
11 1
3 100
4 10
7 20
8 200
14 1000

5 104
3 90
103 89
2 87
99 86
98 85
=263

4 3
6 13
4 8
3 6
5 12
=6

4 3
6 13
4 8
10 6
5 12
=0

4 7
6 13
4 8
3 6
5 12
=14

5 7
2 10
6 13
4 8
3 6
5 12
=22

7 100
100 1
1 100
2 100
3 100
4 100
90 1
5 100
=500

6 100
99 1
1 2
20 3
4 5
80 100
1 300
=407
"""