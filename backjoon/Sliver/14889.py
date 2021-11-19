# 실버3
# 스타트와 링크
import sys
import itertools
N = int(sys.stdin.readline())
T = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
n_list = [i for i in range(N)]

def team_avility_sum(team):
    avility_sum = 0

    for i in team:
        for j in team:
            if i == j: continue
            avility_sum += int(T[i][j])
    return avility_sum

count = N//2
team_list = list(itertools.combinations(n_list, count))

result = []
for i in range(len(team_list)//2):
    # 팀1의 능력치 합 - 팀2의 능력치 합 
    diff_abs = abs(team_avility_sum(team_list[i]) - team_avility_sum(team_list[len(team_list)-(i+1)]))
    result.append(diff_abs)

print(min(result))

"""
반례
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
=0

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0
=2

8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
=1
"""