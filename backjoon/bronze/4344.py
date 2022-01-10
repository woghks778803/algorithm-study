# 브론즈1
# 평균은 넘겠지
N = int(input())

for i in range(N):
    T = list(map(int, input().split()))
    avg = sum(T[1:])/T[0]

    filter_avg = [i for i in filter(lambda x : x>avg, T[1:])]
    print(f"{round((len(filter_avg)/T[0]) * 100, 3):.3f}%")

"""
5
5 50 50 70 80 100
7 100 95 90 80 70 60 50
3 70 90 80
3 70 90 81
9 100 99 98 97 96 95 94 93 91
"""