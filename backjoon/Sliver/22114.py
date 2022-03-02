# 실버2
# 창영이와 점프
# import random
N, K = map(int, input().split())
T = [int(i) for i in input().split()]

val = 1
end = 1
result = []
chance = False
for start in range(N-1):
    while end < N:
        if T[end-1] <= K: # 간격이 좁다면
            val += 1
        elif T[end-1] > K and not chance:
            val += 1
            chance = True
        elif T[end-1] > K and chance:
            break

        end += 1

    result.append(val)
    if T[start] > K and chance: chance = False
    val -= 1

print(max(result))

# T = [random.randrange(1, 7) for i in range(N)]
# print(T)
# print(result)
"""
7 3
2 3 1 5 3 5
"""