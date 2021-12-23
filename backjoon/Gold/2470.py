# 골드5
# 두 용액
# import random
# T = [random.randrange(1, 1000000000) for _ in range(N)]
N = int(input())
T = list(map(int, input().split()))
T = sorted(T)

# 투 포인터
# 이분탐색
zero_diff = 2000000000
result = [T[0], T[-1]]
start = 0
end = len(T) - 1
while start < end:
    if zero_diff == 0: break

    abs_calcu = abs(0 - (T[start] + T[end]))
    if zero_diff > abs_calcu:
        zero_diff = abs_calcu
        result = [T[start], T[end]]

    if 0 < T[start] + T[end]:
        end -= 1
    else:
        start += 1

print(result[0], result[1])
# print(T)

"""
5
-2 4 -99 -1 98

9
-130 -100 0 2 4 13 14 107 1013
"""