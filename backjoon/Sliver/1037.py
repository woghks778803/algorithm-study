# 실버5
# 약수
yaksu_num = int(input())

yaksu_list = list(map(int, input().split()))
yaksu_list.sort()

if yaksu_num % 2 == 1:
    # 중간값 구하기
    mid = yaksu_list[int(yaksu_num/2)]
    print(mid*mid)
else:
    # 최댓값 최솟값 곱하기
    print(max(yaksu_list) * min(yaksu_list))

print(yaksu_list)
