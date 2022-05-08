# 실버1
# 정수 수열
if __name__ == "__main__":
    INF = 100
    x, y, n1, n2, n = map(int, input().split())
    n1 = n1%INF
    n2 = n2%INF

    DP = [[False for _ in range(100)] for _ in range(100)]
    point = 1
    arr = [n1, n2]
    DP[n1][n2] = point

    while True:
        next_num = (x*arr[point] + y*arr[point-1])%INF
        point += 1

        if n == point:
            print(next_num)
            break
        elif DP[arr[point-1]][next_num]:
            start = DP[arr[point-1]][next_num]-1
            end = point-1
            n -= start
            lst = arr[start:end]

            result_point = n%(end-start)
            print((x*arr[result_point] + y*arr[result_point-1])%INF)
            break
        else:
            arr.append(next_num)
            DP[arr[point-1]][next_num] = point


"""
1 1 00 01 10

1 2 01 01 10
"""


    