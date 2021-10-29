# 실버2
# 회의실 배정
import sys
scrum_count = int(input())
scrum_list = []
for i in range(scrum_count):
    scrum_list.append(list(map(int, sys.stdin.readline().split())))

scrum_list.sort(key=lambda x : (x[1], x[0]))
result_list = []
end_time = 0
for i in range(len(scrum_list)):
    if scrum_list[i][0] >= end_time: # 마지막 실행시간보다 회의 시작시간이 같거나 큰 경우
        result_list.append(scrum_list[i])
        end_time = scrum_list[i][1]
    else:
        pass

print(len(result_list))

"""
반례

11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14

13
1 4
3 5
3 6
0 6
5 7
3 8
5 9
6 10
8 11
2 6
8 12
2 13
12 14

5
8 10
3 3
4 7
0 3
5 6

6
8 10
1 5
4 7
0 1
1 1
5 6

"""