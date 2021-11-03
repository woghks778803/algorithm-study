# 브론즈1
# 달팽이는 올라가고 싶다
import math
A, B, V = map(int, input().split())
print(math.ceil((V-A)/(A-B))+1)


"""
2 1 5
5 1 6
100 99 1000000000
"""