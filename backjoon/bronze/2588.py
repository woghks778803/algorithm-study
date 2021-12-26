# 브론즈4
# 곱셈
a = int(input())
b = int(input())
b_split = list(map(int, str(b)))

for i in reversed(b_split): print(a*i)
print(a*b)
