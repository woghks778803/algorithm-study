# 실버4
# 수들의 합2
# 투포인터
N, M = map(int, input().split())
numbers = list(map(int, input().split()))

start = 0
end = 0
result = 0
cnt = 0

while True:
    if result < M:
        if end == N: break
        result += numbers[end]
        end += 1
    else:
        if start == end: break
        result -= numbers[start]
        start += 1

    if result == M:
        cnt += 1
    
print(cnt)

"""
4 2
1 1 1 1

10 5
1 2 3 4 2 5 3 1 1 2
"""
