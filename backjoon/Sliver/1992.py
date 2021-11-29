# 실버1
# 쿼드트리
import sys
N = int(sys.stdin.readline())
T = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]

def dfs(x1, x2, y1, y2):
    w_cnt = 0
    b_cnt = 0
    for i in range(x1, x2):
        for j in range(y1, y2):
            if T[j][i] == 0:
                w_cnt += 1
            else:
                b_cnt += 1

    if w_cnt > 0 and b_cnt > 0:
        print("(",end="")
        dfs(x1, (x1+x2)//2, y1, (y1+y2)//2)
        dfs((x1+x2)//2, x2, y1, (y1+y2)//2)
        dfs(x1, (x1+x2)//2, (y1+y2)//2, y2)
        dfs((x1+x2)//2, x2, (y1+y2)//2, y2)
        print(")",end="")
    elif w_cnt > 0:
        print(0,end="")
    elif b_cnt > 0:
        print(1,end="")

dfs(0, N, 0, N)

"""
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011

8
00000000
00000000
00001111
00001111
00011111
00111111
00111111
00111111

"""