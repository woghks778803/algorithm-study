# 골드3
# 저울
N = int(input())
T = [int(i) for i in input().split()]
T.sort()
DP = [0 for _ in range(N)]
DP[0] = T[0]

if T[0] != 1:
    print(1)
else:
    stop_check = False
    for i in range(1, N):
        if DP[i-1]+1 < T[i]:
            print(DP[i-1]+1)
            stop_check = True
            break
        else:
            DP[i] = DP[i-1] + T[i]

    if not stop_check:
        print(DP[-1]+1)
"""
7
3 1 6 2 7 30 1

7
1 3 2 4 10 20 40

10
1 3 5 7 9 20 31 50 49 130

10
1 2 4 7 9 20 31 50 49 130
"""