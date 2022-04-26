# 실버5
# 성적 통계
K = int(input())
for cl in range(1, K+1):
    T = [int(i) for i in input().split()]
    scores = sorted(T[1:], reverse=True)
    
    diff = 0
    for i in range(1, T[0]):
        temp_diff = scores[i-1] - scores[i]
        if temp_diff > diff: diff = temp_diff

    print(f"Class {cl}")
    print(f"Max {scores[0]}, Min {scores[-1]}, Largest gap {diff}")

"""
2
5 30 25 76 23 78
6 25 50 70 99 70 90
5 1 4 3 2 5
"""