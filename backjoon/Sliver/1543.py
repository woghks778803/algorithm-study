# 실버4
# 문서 검색
S = input()
V = input()
i = 0
cnt = 0
result = 0
while i < len(S):
    if V[cnt] == S[i]: 
        cnt += 1
    else: 
        i = i-cnt
        cnt = 0

    if cnt >= len(V):
        cnt = 0
        result += 1
    i+=1
print(result)

"""
ababababa
aba
ababababa
ababa
ababaa
abaa
"""