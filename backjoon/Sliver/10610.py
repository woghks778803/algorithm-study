# 실버5
# 30
N = input()
result = int(''.join(sorted(N, reverse=True)))

if result%30 != 0: print(-1)
else: print(result)

"""
41166010
66411100
2010
3210
96240
"""