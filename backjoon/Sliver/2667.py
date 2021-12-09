# 실버1
# 단지번호붙이기
N = int(input())
T = [list(map(int, input())) for _ in range(N)]
visit_check = [[False for _ in range(N)] for _ in range(N)]
x_p = [0, 0, -1, 1]
y_p = [-1, 1, 0, 0]
result = []

def dfs(x, y):
    if T[y][x] == 1 and visit_check[y][x] == False:
        global count
        count += 1
        visit_check[y][x] = True

        for k in range(len(x_p)):
            if N > y+y_p[k] >= 0 and N > x+x_p[k] >= 0:
                dfs(x+x_p[k], y+y_p[k])

for y in range(N):
    for x in range(N):

        if T[y][x] == 1 and visit_check[y][x] == False:
            count = 1
            visit_check[y][x] = True

            for k in range(len(x_p)):
                if N > y+y_p[k] >= 0 and N > x+x_p[k] >= 0:
                    dfs(x+x_p[k], y+y_p[k])

            result.append(count)

result.sort()
print(len(result))
for i in result: print(i)   
         

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
"""