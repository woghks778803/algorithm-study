# 실버5
# 캠핑
cnt = 0
while True:
    cnt += 1
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0: break

    if (V%P)//L >= 1:
        print(f"Case {cnt}: {(V//P)*L + L}")
    else:
        print(f"Case {cnt}: {(V//P)*L + (V%P)%L}")

"""
5 8 20
5 8 17
0 0 0
"""