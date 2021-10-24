# 브론즈1
# 수 정렬하기
test_case_cnt = int(input())
test_case = []
for i in range(test_case_cnt):
    test_case.append(int(input()))

test_case.sort()
for i in test_case:
    print(i)