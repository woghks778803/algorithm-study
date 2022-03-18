# 골드5
# 1학년
def solve(standard):
    for i in range(1, N-1):

        for j in range(21):
            if 20 >= j+T[i] >= 0:
                DP[i][j+T[i]] += DP[i-1][j]

            if 20 >= j-T[i] >= 0:
                DP[i][j-T[i]] += DP[i-1][j]

    print(DP[N-2][standard])    

if __name__ == "__main__":
    N = int(input())
    T = [int(i) for i in input().split()]
    standard = T.pop()

    DP = [[0 for _ in range(21)] for _ in range(N)]
    DP[0][T[0]] = 1
    solve(standard)


"""
11
8 3 2 4 8 7 2 4 0 8 8

40
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 1 1
"""