# 브론즈2
# 숫자의 개수
T = [int(input()) for _ in range(3)]
num = 1
for i in T: num *= i
lst = list(map(int, str(num)))
for i in range(10): print(lst.count(i))

"""
150
266
427
"""