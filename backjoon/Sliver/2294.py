# 실버1
# 동전 2
import sys
N, K = map(int, sys.stdin.readline().split())
INF = 100001
T = [int(sys.stdin.readline()) for _ in range(N)] # 값이 정렬되어있지않음
DP = [INF for _ in range(K+1)]

for i in range(1, K+1):
    for j in range(N):
        if i == T[j]: 
            DP[i] = 1
            break # 1보다 낮은 경우의 수는 없으니 해당 루프 탈출
        if K < T[j]: continue # 기준값 초과로 제외 처리

        DP[i] = min(DP[i], DP[i-T[j]]+1) # 현재 dp값과 t[j] 값을 뺀 이전 dp값이 비교

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