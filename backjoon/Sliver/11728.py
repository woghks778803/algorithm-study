# 실버5
# 배열 합치기
N, M = map(int, input().split())
result = []

a = map(int, input().split())
b = map(int, input().split())

for ele in a: result.append(ele)
for ele in b: result.append(ele)
result.sort()
print(str(result).replace('[','').replace(']','').replace(',',''))

"""
2 2
3 5
2 9

4 3
2 3 5 9
1 4 7

2 1
4 7
1
"""