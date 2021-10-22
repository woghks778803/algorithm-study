# 실버3
# 단어 뒤집기 2
test_case = list(input())
chk_open = False
temp_str_list = []
result_list = []

def list_clear():
    if len(temp_str_list) != 0:
        if chk_open == False:
            temp_str_list.reverse()
        temp_str = ""
        for j in temp_str_list:
            temp_str += j
        result_list.append(temp_str)
        temp_str_list.clear()

count = 0
for case_str in test_case:
    count += 1
    if case_str == " " and chk_open == True:
        temp_str_list.append(case_str)
    elif case_str == " " and chk_open == False:
        list_clear()
        result_list.append(case_str)
    elif case_str == "<":
        # 이전 문자 리스트 저장 후 임시 문자 제거
        list_clear()
        # 현재 문자 저장
        temp_str_list.append(case_str)
        chk_open = True
    elif case_str == ">":
        temp_str_list.append(case_str)
        list_clear()
        chk_open = False
    else:
        temp_str_list.append(case_str)

    if len(test_case) == count and case_str != ">":
        list_clear()

result = ""
chk_meta = False
# 결과 출력
for result_str in result_list:
    result += result_str
print(result)