# 실버4
# 소가 길을 건너간 이유 3
N = int(input())
T = [[int(i) for i in input().split()] for _ in range(N)]
T.sort(reverse=True)

time = 0
while T:
    cow = T.pop()
    if cow[0] >= time: time = cow[0]
    time += cow[1]

print(time)


"""
3
2 1
8 3
5 7
"""