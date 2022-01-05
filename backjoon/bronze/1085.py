# 브론즈3
# 직사각형에서 탈출
x, y, w, h = map(int, input().split())

print(min(w-x, h-y, x, y))

"""
6 2 10 3
1 1 5 5
653 375 1000 1000
161 181 762 375
"""