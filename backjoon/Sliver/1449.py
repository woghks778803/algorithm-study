# 실버3
# 수리공 항승
N, L = map(int, input().split())
T = [int(i) for i in input().split()]
T.sort()

result = start = end = 0
for i in T:
    if start == 0 or end < i:
        result += 1
        start = i
        end = i+(L-1)
print(result)

"""
4 2
1 2 100 101

4 3
1 2 3 4

3 1
3 2 1
"""