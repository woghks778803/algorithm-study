# 실버4
# 병든 나이트
N, M = map(int, input().split())
result = 1

if N == 2:
    if M >= 7: result = 4
    else: result += (M-1)//2
elif N > 2:
    if M < 7:
        if M >= 4: result = 4
        else: result = M
    else:
        result = M-2

print(result)