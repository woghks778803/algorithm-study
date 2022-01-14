# 브론즈2
# 문자열 반복
import sys
T = int(input())
for _ in range(T):
    R, S = map(str, input().split())
    S = list(S)

    for i in S:
        for _ in range(int(R)):
            sys.stdout.write(i)
    print()


"""
2
3 ABC
5 /HTP

1
4 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./

1
4 XYZ\
"""