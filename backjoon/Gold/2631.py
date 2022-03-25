# 골드5
# 줄세우기
def LIS():
    for i in range(1, N):
        for j in range(i):
            if T[i] > T[j]:
                DP[i] = max(DP[i], DP[j]+1)

    print(N-max(DP))

if __name__ == "__main__":
    N = int(input())
    T = [int(input()) for _ in range(N)]
    DP = [1 for _ in range(N)]

    LIS()

"""
7
3
7
5
2
6
1
4
"""