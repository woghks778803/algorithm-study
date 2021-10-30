# 실버2
# 잃어버린 괄호
test_case = input()

num = test_case.replace('+', '-')
num = num.split('-')

check_num_str = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
sign_str = test_case
for i in check_num_str:
    sign_str = sign_str.replace(str(i), "")

sign_list = list(sign_str)

formula = ""
# 이전에 괄호가 생성되었는지 체크
open_check = False
# 괄호 넣기
for i in range(len(sign_list)):
    int_num = str(int(num[i]))
    if i == len(sign_list)-1: # 마지막 순번인 경우
        if open_check == True and sign_list[i] == '-':
            # 괄호 닫기
            open_check = False
            formula += int_num
            formula += ")"
            formula += sign_list[i]
        else:
            formula += int_num
            formula += sign_list[i]
    else:
        # 현재 수식이 -인 경우
        if sign_list[i] == '-':
            # 다음 수식이 -인 경우
            if sign_list[i+1] == '-' and open_check == True:
                # 괄호 닫기
                open_check = False
                formula += int_num
                formula += ")"
                formula += sign_list[i]
            elif sign_list[i+1] == '-' :
                formula += int_num
                formula += sign_list[i]
            elif sign_list[i+1] == '+' and open_check == True:
                # 괄호 닫고 다시 열기
                formula += int_num
                formula += ")"
                formula += sign_list[i]
                formula += "("
            else:
                # 괄호 추가 
                open_check = True
                formula += int_num
                formula += sign_list[i]
                formula += "("
        else:
            formula += int_num
            formula += sign_list[i]
        
formula += str(int(num[len(sign_list)]))
if open_check == True:
    formula += ")"
print(eval(formula))

"""
반례

55-50+40

10+20+30+40

00009-00009

0-8994+8+00-610+722+6691-482+65-3
-17575
9-4606+4-2-44-3-5442+2453+9-55
-12609
4-662+1067+0+4-85-7993+4+9432+139
-19382
3-6-5-75+991-6310-331+844-196+3
-8758
1-76+77-16-213+1+8800+61-776-18
-10037
6-3+5+6-8
-16
5+4-2+9+8
-10
1-8+1-8-8
-24
5-8+5+4+7
-19
8-2+1-4+8
-7
5-4+5
-4
7-6+7
-6
5-8+5
-8
5-2+5
-2
2-9+2
-9
"""