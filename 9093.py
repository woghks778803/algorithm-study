# 브론즈1
# 단어 뒤집기
test_case_cnt = int(input())
str_list = []

for i in range(0, test_case_cnt):
    # 문장 입력받기
    input_strs = list(map(str, input().split()))

    # 문장 단어별 알파벳 역순 저장
    reverse_str_list = []
    for input_str in input_strs:
        reverse_str = list(input_str)
        reverse_str.reverse()
        reverse_str_list.append(reverse_str)

    str_list.append(reverse_str_list)

# 역순 저장 리스트 문장단위 출력
for reverse_str_list in str_list:
    str_message = ""
    for reverse_str in reverse_str_list:
        str_word = ""
        for reverse_char in reverse_str:
            str_word += reverse_char
        str_message += str_word + " "
    print(str_message)
        
