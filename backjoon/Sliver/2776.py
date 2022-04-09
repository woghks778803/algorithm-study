# 실버4
# 암기왕
T = int(input())

for _ in range(T):
    N = int(input())
    T1 = [int(i) for i in input().split()]
    T1.sort(reverse=True)

    M = int(input())
    T2 = [int(i) for i in input().split()]
    temp = T2.copy()
    T2.sort(reverse=True)

    t1 = T1.pop()
    t2 = T2.pop()
    result = {}
    while True:

        if t1 == t2:
            result[t1] = True

            if T1: t1 = T1.pop()
            else: break
            if T2: t2 = T2.pop()
            else: break

        elif t1 < t2:
            if T1: t1 = T1.pop()
            else: break
        else:
            if T2: t2 = T2.pop()
            else: break

    for t in temp:
        if result.get(t): print(1)
        else: print(0)


"""
1
5
4 1 5 2 3
5
1 3 7 9 5

2
5
1 5 7 8 9
5
1 5 6 7 7
"""