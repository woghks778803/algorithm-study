# 실버4
# 보물
if __name__ == "__main__":
    N = int(input())
    A = [int(i) for i in input().split()]
    B = [int(i) for i in input().split()]
    A.sort()
    B.sort(reverse=True)

    result = 0
    for i in range(N): result += A[i] * B[i]

    print(result)

"""
5
1 1 1 6 0
2 7 8 3 1

3
1 1 3
10 30 20

9
5 15 100 31 39 0 0 3 26
11 12 13 2 3 4 5 9 1
"""