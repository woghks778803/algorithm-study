# 실버4
# 로프
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    N = int(input())
    T = [int(input()) for _ in range(N)]
    T.sort()

    result = 0
    for i in range(N):
        culc = T[i]*(N-i)
        if culc > result: result = culc
    print(result)

"""
2
10
15

3
100
80
20
"""