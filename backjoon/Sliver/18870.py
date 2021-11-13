# 실버2
# 좌표 압축
import sys
test_case_cnt = int(input())
test_case = list(map(int, sys.stdin.readline().split()))

# 좌표압축 알고리즘 = 값은 인덱스로 변환한다
test_case_index = sorted(list(set(test_case)))
dic = {test_case_index[i] : i for i in range(len(test_case_index))} # 신기하네..

for i in test_case:
    print(dic[i], end=" ")
    # test_case_index.index(test_case[i])를 사용할 경우 매번 인덱스 검사를 진행해서 성능이 느리니 dictionary로 찾아야한다
    # 인덱스 검사(시간복잡도 O(N)) = 갯수가 100000개라면 매번 100000번 검사 실행
    

