# 골드3
# 줄 세우기
N = int(input())
DP = [0 for _ in range(N+1)]
for i in input().split():
    int_a = int(i)
    DP[int_a] = DP[int_a-1] + 1

print(N - max(DP))

"""
5
5 2 4 1 3

8
3 7 4 5 6 2 1 8
"""