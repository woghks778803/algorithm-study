# 실버3
# 나무 자르기
N, M = map(int, input().split())
T = list(map(int, input().split()))

max_h = max(T)
min_h = 0
mid_h = (max_h+min_h)//2
while min_h <= max_h:
    sum_len = 0
    for i in T:
        if i - mid_h > 0: sum_len += i - mid_h

    if sum_len > M:
        min_h = mid_h+1
        mid_h = (max_h+min_h)//2
    elif sum_len < M:
        max_h = mid_h-1
        mid_h = (max_h+min_h)//2
    else: break

print(mid_h)
# 내 코드가 정답이야 -ㅅ-
"""
4 7
20 15 10 17

5 20
4 42 40 26 46

5 1
4 42 40 26 43

2 11
10 10

2 1
5 5

5 20
4 42 40 26 44
"""