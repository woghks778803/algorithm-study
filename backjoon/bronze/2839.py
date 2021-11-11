# 브론즈1
# 설탕 배달
N = int(input())
result = 0

max_share = []
if N % 5 == 0:
    result += N // 5
else:
    share = N // 5
    for i in reversed(range(0, share+1)):
        remainder = N - (i*5)
        if remainder % 3 == 0: max_share.append(i+(remainder // 3))

if len(max_share) != 0: result += min(max_share)

if result == 0: print(-1)
else: print(result)


"""
반례
18
=4
4
=-1
6
=2
11
=3
16
=4
"""

    



