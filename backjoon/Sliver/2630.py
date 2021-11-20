# 실버3
# 색종이 만들기
import sys
N = int(sys.stdin.readline())

T = []
for _ in range(N):
    T.append(list(map(int, sys.stdin.readline().split())))

def dfs(r1, r2, c1, c2):
    if r2 - r1 <= 1 or c2 - c1 <= 1:
        global blue, white
        if T[r1][c1] == 1: blue += 1
        else: white += 1
        return True

    bcnt = 0
    wcnt = 0
    for i in range(r1, r2):
        for j in range(c1, c2):
            if T[i][j] == 1: bcnt += 1
            else: wcnt += 1

            if bcnt > 0 and wcnt > 0:
                dfs(r1, (r1+r2)//2, c1, (c1+c2)//2)
                dfs(r1, (r1+r2)//2, (c1+c2)//2, c2)
                dfs((r1+r2)//2, r2, c1, (c1+c2)//2)
                dfs((r1+r2)//2, r2, (c1+c2)//2, c2)
                return True

    if bcnt: blue += 1
    else: white += 1

white = 0
blue = 0
dfs(0, N, 0, N)
print(white)
print(blue)


"""
4
1 1 0 0
1 1 0 1
1 0 0 0
0 0 0 0

8
1 1 0 0 0 0 1 1
1 1 0 0 0 0 1 1
0 0 0 0 1 1 0 0
0 0 0 0 1 1 0 0
1 0 0 0 1 1 1 1
0 1 0 0 1 1 1 1
0 0 1 1 1 1 1 1
0 0 1 1 1 1 1 1
"""