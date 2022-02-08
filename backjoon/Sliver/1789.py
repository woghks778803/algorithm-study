# 실버5
# 수들의 합
S = int(input())

i = 1
while True:
    S -= i

    if S < 0:
        print(i-1)
        break
    i += 1

"""
4294967295
"""