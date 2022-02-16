# 골드5
# 센서
N = int(input())
K = int(input())
T = [int(i) for i in input().split()]
T.sort()
# T = list(set(T))

# 각 지점별 거리차 구하기
diff = []
for i in range(1, len(T)):
    diff.append(abs(T[i-1] - T[i]))

diff.sort()
# K개의 묶음이기 때문에 거리가 가장 먼 K-1개를 제외하고 모든 거리를 더하기 
print(sum(diff[:len(diff)-(K-1)]))
# print(diff[:len(diff)-(K-1)])
# print(T)
# print(diff)


"""
6
2
1 6 9 3 6 7

10
5
20 3 14 6 7 8 18 10 12 15

16
3
1 4 7 8 9 10 12 14 17 18 20 21 24 25 28 29
"""