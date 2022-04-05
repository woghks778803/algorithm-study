# 실버3
# 가장 긴 짝수 연속한 부분 수열 (small)
N, K = map(int, input().split())
T = [int(i) for i in input().split()]
DP = [0 for _ in range(N)]

# 투 포인터
end = 0
result_cnt = 0
remove_cnt = 0
for start in range(N):
    while end < N and remove_cnt <= K:
        if T[end]%2 == 0:
            result_cnt += 1
        else:
            remove_cnt += 1

        end += 1

    DP[start] = max(DP[start], result_cnt)
    if T[start]%2 == 0: result_cnt -= 1
    else: remove_cnt -= 1

print(max(DP))
# print(DP, result_cnt)


"""
8 2
1 2 3 4 5 6 7 8
0 1 1 2 2 3 3 
1 1 2 2 3 2 3

11 2
1 2 3 4 6 7 8 9 10 12 14
"""