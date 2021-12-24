# 골드4
# 부분합
N, S = map(int, input().split())
num_list = list(map(int, input().split()))

end = 0
count = 0
interval_sum = 0
count_list = []

# 투 포인터
# start를 차례대로 증가시키며 반복
for start in range(N):
    # end만큼 이동시키기
    while interval_sum < S and end < N:
        interval_sum += num_list[end]
        count += 1
        end += 1

    # 부분합이 S이상일 때 카운트 저장
    if interval_sum >= S:
        count_list.append(count)
    
    interval_sum -= num_list[start]
    count -= 1

if len(count_list) == 0:
    print(0)
elif S == 0 and max(num_list) > 0:
    print(1)
else:
    print(min(count_list))


"""
반례

10 21
11 2 5 6 8 9 2 3 10 9
3

10 30
11 2 5 6 8 9 2 3 10 9
5

14 114
11 12 13 14 15 16 17 18 25 26 27 28 29 30
4

11 38
11 2 5 6 8 9 2 3 10 9 10
6

10 189

10 15
5 1 3 5 10 7 4 9 2 8
2

10 0
1 1 1 1 1 1 1 1 1 1
1

6 1
2 2 2 2 2 2
1

6 1
3 2 2 2 2 2
1

10 100
5 1 3 5 10 7 4 9 2 8
0

6 15
1 1 5 8 1 1
4
"""



