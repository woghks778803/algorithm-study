# 브론즈3
# 직각삼각형
while True:
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0: break

    arr = [a, b, c]
    arr.sort()
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        print("right")
    else:
        print("wrong")

"""
6 8 10
25 52 60
5 12 13
0 0 0
"""