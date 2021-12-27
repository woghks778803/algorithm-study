# 실버4
# 한수
N = int(input())
ans = 0
for i in range(1, N+1):
    if i < 10: 
        ans += 1
    else:
        num = list(map(int, str(i)))
        diff = set([num[i] - num[i - 1] for i in range(1, len(num))])
        if len(diff) == 1: ans += 1

print(ans)



