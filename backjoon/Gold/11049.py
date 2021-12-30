# 골드3
# 행렬 곱셈 순서
# X
N = int(input())
DP = [[0 for _ in range(N)] for _ in range(N)]
arr = [0 for _ in range(N+1)]

for i in range(1, N+1):
    a, b = map(int, input().split())
    arr[i-1] = a
    arr[i] = b

for i in range(1, N): # 2개 행렬곱셈 초기값
    DP[i-1][i] = arr[i-1] * arr[i] * arr[i+1]

for size in range(1, N): # 행렬곱셈 초기값 갯수 (n-1)
    for start in range(N-size): 
        min_num = 2**31
        for k in range(start, start+size):
            cost = DP[start][k] + DP[k+1][start+size] + arr[start] * arr[k+1] * arr[start+size+1]

            if min_num>cost: min_num = cost
        DP[start][start+size] = min_num

print(DP[0][-1])

"""
3
5 3
3 2
2 6
"""