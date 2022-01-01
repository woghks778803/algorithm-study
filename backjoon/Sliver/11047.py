# 실버2
# 동전 0
N, K = map(int, input().split())

# 입력값 리스트 저장
T = [int(input()) for _ in range(N)]
T.sort()

result = []
for i in range(1, N+1):
    temp_k = K
    cnt = 0
    for j in range(N-i, -1, -1):
        if T[j] > temp_k: pass
        else: 
            cnt += temp_k // T[j]
            temp_k = temp_k % T[j]

    if temp_k == 0:
        result.append(cnt)
        
if not result:
    print(-1)
else:
    print(min(result))


# 반례
"""
4 1300
1000
70
10
1
= 7

4 4200
3
99
700
1000

6 2430
1 
300 
1800 
7200 
14400
28800

6 360
1
15
60
300
1500
4500

10 4200
1
10
5
100
500
50
1000
5000
10000
50000

4 4200
1000
700
99
3

5 1000
1
20
100
500
1000

10 3600
1
12
36
144
720
3600
36000
108000
216000
864000
"""