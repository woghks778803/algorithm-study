# 실버1
# 퇴사 2
import sys
N = int(sys.stdin.readline())
DP = [0 for _ in range(N)]
T = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    T.append([a, b])

for remain_day in range(1, N+1):
    cur_day = N-remain_day # 현재날짜
    deadline = cur_day +T[cur_day][0] # 당일 업무 소요시간과 현재날짜
    if remain_day == 1:
        if deadline <= N: DP[cur_day] = T[cur_day][1]
    elif deadline > N:
        DP[cur_day] = DP[cur_day+1]
    elif deadline == N: # 당일 업무량과 이전값의 합과 비교
        DP[cur_day] = max(DP[cur_day+1], T[cur_day][1])
    else:
        DP[cur_day] = max(DP[cur_day+1], T[cur_day][1] + DP[deadline])

print(max(DP))
print(DP)
print(T)
"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
"""