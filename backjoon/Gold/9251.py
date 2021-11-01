# 골드5
# LCS
test_case = []
test_case.append(list(input()))
test_case.append(list(input()))
intersection = set(test_case[0]) & set(test_case[1])

if len(intersection) == 0:
    print(0)
else:
    x_len = len(test_case[0])+1
    y_len = len(test_case[1])+1
    long_length = 0
    LCS = [[0 for i in range(x_len)] for j in range(y_len)]

    for i in range(1, y_len):
        for j in range(1, x_len):
            if test_case[0][j-1] == test_case[1][i-1]:
                LCS[i][j] = LCS[i-1][j-1] + 1
                if LCS[i][j] > long_length:
                    long_length = LCS[i][j]
            else:
                LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])

    print(long_length)


"""
ACAYKP
CAPCAK

ABCD
EFGH

GDGVSYREB
JJSKRSJEE

GJEUFJ
JDKEJF

YYYYABCD
ABCDNNNN

GJEUFJABCD
JDKABCDEJF

ABCDEF
FEDCBA

XFXXXQ
XXXXXF

XFXFXXQ
XXXXXFF

XXXXXFF
XFFXXXQ
"""