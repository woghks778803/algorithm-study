# 실버1
# 연산자 끼워넣기
import itertools
N = int(input())
num_list = list(map(int, input().split()))
sign = list(map(int, input().split()))

def division(num1, num2):
    if num1<0:
        return (abs(num1)//num2)*(-1)
    else:
        return num1//num2

sign_list = []
for i in range(len(sign)):
    for j in range(sign[i]):
        sign_list.append(str(i))

result = []
# sign_order = itertools.permutations(sign_list, len(sign_list))
sign_order = list(map(''.join, itertools.permutations(sign_list, len(sign_list))))

# 중복제거
sign_order = set(sign_order)
sign_order = list(sign_order)

for sign in sign_order:

    formula_str = num_list[0]
    for j in range(1, N):
        if sign[j-1] == "0":
            formula_str = formula_str + num_list[j]
        elif sign[j-1] == "1":
            formula_str = formula_str - num_list[j]
        elif sign[j-1] == "2":
            formula_str = formula_str * num_list[j]
        elif sign[j-1] == "3":
            formula_str = division(formula_str,num_list[j])

    result.append(formula_str)

print(max(result))
print(min(result))



"""
2
5 6
0 0 1 0

3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1

2
-9 3
0 0 0 1
"""