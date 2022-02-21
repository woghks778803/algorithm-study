# 골드5
# 주사위
N = int(input())
T = [int(i) for i in input().split()]
min_dice = [min(T[0],T[5]), min(T[1],T[4]), min(T[2],T[3])]
min_dice.sort()

if N == 1:
    print(sum(T)-max(T))
else:
    result = []
    # 1면 노출 (N-1)*(N-2)*4 + (N-2)**2
    result.append(min_dice[0]*(5*N**2-16*N+12))

    # 2면 노출 4(N-2) + 4(N-1)
    result.append((min_dice[0]+min_dice[1])*(8*N-12))
    
    # 3면 노출 각 꼭짓점 4개
    result.append(sum(min_dice)*4)

    print(sum(result))
    # print(result)
"""
2
1 2 3 4 5 6

1000000
50 50 50 50 50 50

10
1 1 1 1 50 1
"""
