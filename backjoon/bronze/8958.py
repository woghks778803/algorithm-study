# 브론즈2
# OX퀴즈
for i in range(int(input())):
    lst = list(input())
    score = 0
    continue_cnt = 0
    for i in lst:
        if i == "O":
            continue_cnt += 1
            score += continue_cnt
        else:
            continue_cnt = 0

    print(score)

"""
5
OOXXOXXOOO
OOXXOOXXOO
OXOXOXOXOXOXOX
OOOOOOOOOO
OOOOXOOOOXOOOOX
"""