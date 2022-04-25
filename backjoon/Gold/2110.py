# 골드5
# 공유기 설치
# X
import sys
input = sys.stdin.readline
N, C = list(map(int, input().split()))
result = 0

T = [int(input()) for i in range(N)]
T.sort()

start = 0
end = T[-1] - T[0]

while start <= end:
    mid = (start+end)//2
    cnt = 1 # 시작점에 공유기 설치

    for i in range(N):
        if i == 0:
            cur = T[i]
        else:
            if T[i] >= cur+mid:
                cnt += 1
                cur = T[i]

    if cnt >= C:
        start = mid+1
        result = mid
    else:
        end = mid-1

print(result)

"""
반례

4 3
1
2
8
9

4 3
11
13
16
18

5 4
30
20
10
5
15

4 3
1
3
5
7

5 4
30
27
11
5
16

5 3
1
7
8
9
10

5 3
1
2
8
4
9
=3

3 3
1
4
6
=2

5 2
1
2
8
4
9
=8

"""
