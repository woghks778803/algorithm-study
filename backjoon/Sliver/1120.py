# 실버4
# 문자열
X, Y = map(str, input().split())
result = []
len_x = len(X)
len_y = len(Y)

for i in range(len_y-len_x+1):
    cnt = 0
    for j in range(len_x):
        if X[j] == Y[j+i]:
            cnt += 1

    result.append(len_x-cnt)

print(min(result))
# print(result)

"""
adaabc aababbc
giorgi igroig
"""