# 골드5
# 합분해
if __name__ == "__main__":
    N, K = map(int, input().split())
    arr = [[1 for _ in range(N)] for _ in range(K)]
    
    for i in range(K): arr[i][0] = i+1

    for i in range(1, K):
        for j in range(1, N):
            arr[i][j] = (arr[i-1][j] + arr[i][j-1]) % 1000000000

    print(arr[-1][-1])