# 실버1
# 카드 구매하기
N = int(input())
T = [int(i) for i in input().split()]
DP = [0 for _ in range(N+1)]

for i in range(1, N+1):
    temp = []
    for j in range(1, i+1):
        temp.append(T[j-1] + DP[i-j])
    DP[i] = max(temp)

print(DP[N])

"""
4
1 5 6 7
5
10 9 8 7 6
10
1 1 2 3 5 8 13 21 34 55
10
5 10 11 12 13 30 35 40 45 47
4
5 2 8 10
4
3 5 15 16
"""
