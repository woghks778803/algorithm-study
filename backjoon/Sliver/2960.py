# 실버4
# 에라토스테네스의 체
def solve(cnt):
    for i in range(2, N+1):
        if T[i]: continue

        for j in range(i, N+1, i):
            if T[j]: 
                continue
            else:
                cnt += 1
                T[j] = True

            if cnt == K:
                return j

N, K = map(int, input().split())
T = [False for _ in range(N+1)]
cnt = 0

result = solve(cnt)
print(result)
print(T)

