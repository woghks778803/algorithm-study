# 실버1
# 동전 2
N, K = map(int, input().split())
INF = 100001
T = [int(input()) for _ in range(N)]
DP = [INF for _ in range(K+1)]

for i in range(1, K+1):
    for j in range(N):
        if i == T[j]: 
            DP[i] = 1
            break

        if K < T[j] or i < T[j]: continue
        DP[i] = min(DP[i], DP[i-T[j]]+1)

if DP[K] == INF:
    print(-1)
else:
    print(DP[K])
# print(DP)


"""
5 1300
1000
70
60
10
1

3 15
1
5
12

5 1300
1000
70
60
10
1
= 6

5 1300
1000
70
60
10
1
= 6

37 5613
87790
43967
559
72151
67275
38910
84025
67209
32377
21308
9286
3383
87781
88748
97756
51628
2340
60417
8975
23368
79102
93121
36903
82895
66167
32839
55158
14845
11282
12749
98911
49607
65978
80144
8161
12970
25526
"""