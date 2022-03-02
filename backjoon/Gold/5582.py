# 골드5
# 공통 부분 문자열
S1, S2 = input(), input()
DP = [[0 for _ in range(len(S1)+1)] for _ in range(len(S2)+1)]
result = 0
for i in range(1, len(S2)+1):
    for j in range(1, len(S1)+1):
        if S1[j-1] == S2[i-1]:
            DP[i][j] = DP[i-1][j-1] + 1
            result = max(DP[i][j], result)

print(result)

"""
ABRACADABRA
ECADADABRBCRDARA

UPWJCIRUCAXIIRGL
SBQNYBSBZDFNEV
"""