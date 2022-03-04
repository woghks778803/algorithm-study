# 실버3
# Maximum Subarray
# 투 포인터 (언젠가 정복해보자..)
# def twoPointer(len_arr, arr):
#     end = 0
#     sum_num = arr[end]
#     result = [sum_num]

#     for start in range(len_arr):
#         if end == start and end < len_arr-1:
#             end += 1
#             sum_num += arr[end]
#             result.append(sum_num)

#         while 0 < sum_num and end < len_arr-1:
#             end += 1
#             sum_num += arr[end]
#             result.append(sum_num)

#         sum_num -= arr[start]
#         result.append(sum_num)

#     print(max(result[:-1]))

# 동적 계획법
def dp(len_arr, arr):
    DP = [0 for _ in range(len_arr)]
    DP[0] = arr[0]

    for i in range(1, len_arr):
        DP[i] = max(arr[i], DP[i-1]+arr[i])
    print(max(DP))

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N = int(input())
        arr = [int(i) for i in input().split()]
        dp(N, arr)
        # twoPointer(N, arr)

"""
6
5
1 2 3 4 5
5
2 1 -2 3 -5
8
-2 1 1 -3 3 5 -5 6
6
-5 5 4 3 2 1
7
-100 10 -100 -100 -50 -40 -30
7
-100 -10 -100 -100 -50 -40 -30
"""