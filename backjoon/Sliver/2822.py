# 실버5
# 점수 계산
T = [[int(input()), i+1] for i in range(8)]
T.sort(key= lambda x : [-x[0]])

sum_num = 0
lst_num = []
for i in range(5):
    sum_num += T[i][0]
    lst_num.append(T[i][1])
lst_num.sort()

print(sum_num)
print(*lst_num)

"""
20
30
50
48
33
66
0
64

20
0
50
80
77
110
56
48
"""