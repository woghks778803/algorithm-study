# 골드5
# LCS 2
import sys
N = list(sys.stdin.readline().strip())
M = list(sys.stdin.readline().strip())
intersection = set(N) & set(M) # 두 수열의 교집합

if len(intersection) == 0: # 두 수열간 같은 값이 존재하지않을경우
    print(0)
else:
    y_len = len(N)+1
    x_len = len(M)+1
    LCS = [ [0 for _ in range(x_len)] for _ in range(y_len) ]

    for i in range(1, y_len):
        for j in range(1, x_len):
            
            if N[i-1] == M[j-1]: # 수열의 값이 일치할 경우
                LCS[i][j] = LCS[i-1][j-1]+1
            else:
                LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])

    # 초기 기준값
    move_x = x_len-1
    move_y = y_len-1
    standard = LCS[move_y][move_x]
    result_str = []

    while True:
        if LCS[move_y][move_x-1] == standard: # 인접 길이 값 중 동일한 값이 있을경우 해당 위치로 이동
            move_x -= 1
        elif LCS[move_y-1][move_x] == standard:
            move_y -= 1
        else:
            # 인접 길이 값 중 중 동일한 값이 없을경우 대각선 이동
            move_x -= 1
            move_y -= 1
            standard = LCS[move_y][move_x]
            result_str.append(N[move_y])
        
        # 최장 길이 값에 도달할 경우
        if len(result_str) >= LCS[-1][-1]: break

    print(LCS[-1][-1])
    for _ in reversed(result_str): sys.stdout.write(_)
    # print(result_str)
    # print(LCS)

"""
ACAYKP
CAPCAK
"""