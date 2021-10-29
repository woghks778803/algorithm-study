# 실버3
# 1,2,3 더하기
test_case_cnt = int(input())
test_case_list = []

# 재귀함수 선언
def add(sum, test_case):
    if sum > test_case:
        return
    elif sum == test_case:
        global count # 전역변수 호출
        count += 1
        return
    else:
        for i in range(1,4):
            add(sum+i, test_case)

# 입력값 리스트 저장
for i in range(test_case_cnt):
    test_case_list.append(int(input()))

# test_case별 실행
for test_case in test_case_list:
    count = 0 # 전역변수 선언
    add(0, test_case)
    print(count)

