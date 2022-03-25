# 실버5
# 뒤집기
T = [int(i) for i in list(input())]
result = [0, 0]
standard = T[0]
if standard == 0: result[0] += 1
else: result[1] += 1

for i in range(len(T)):
    if standard != T[i]:
        standard = T[i]
        if standard == 0: result[0] += 1
        else: result[1] += 1
        
print(min(result))


"""
0001100
11101101
"""