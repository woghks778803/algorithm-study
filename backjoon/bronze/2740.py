# 브론즈1
# 행렬 곱셈
import sys
temp = []
rule = []
for _ in range(2):
    N, M = map(int, sys.stdin.readline().split())
    rule.append([N, M])
    a = [[] for _ in range(N)]
    for i in range(N):
        temp_list = list(map(int, sys.stdin.readline().split()))
        for j in range(M): a[i].append(temp_list[j])
    temp.append(a)

N, M, K = rule[0][0], rule[0][1], rule[1][1]
result = []
for i in range(N):
    line_list = []
    for k in range(K):
        line_ele = 0
        for j in range(M): line_ele += temp[0][i][j]*temp[1][j][k]
        line_list.append(line_ele)
    result.append(line_list)

for result_ele in result:
    for i in result_ele: sys.stdout.write(str(i)+" ")
    sys.stdout.write("\n")