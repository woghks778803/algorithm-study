# 골드3
# 소수의 연속합
N = int(input())
T = [True for _ in range(N+1)]
T[0] = False
T[1] = False
sosu = []

# 에라토스테네스의 체
for i in range(2, N+1):
    if not T[i]: continue
    else: sosu.append(i)

    for j in range(i*2, N+1, i): T[j] = False

del T

# 투 포인터 알고리즘
interval_sum = 0
end = 0
count = 0
for start in range(len(sosu)):
    while interval_sum < N and end < len(sosu):
        interval_sum += sosu[end]
        end += 1

    if interval_sum == N:
        count += 1
    interval_sum -= sosu[start]

print(count)


"""
3999971
= 2

20
3
41
53
"""