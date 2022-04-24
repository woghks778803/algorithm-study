# 실버3
# 수열
N, K = map(int, input().split())
T = [int(i) for i in input().split()]

result = sum(T[:K])
temp = result
for i in range(K, N):
    temp = temp - T[i-K] + T[i]
    if result < temp: result = temp

print(result)

"""
10 2
3 -2 -4 -9 0 3 7 13 8 -3

10 5
3 -2 -4 -9 0 3 7 13 8 -3
"""