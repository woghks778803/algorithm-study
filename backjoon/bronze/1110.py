# 브론즈1
# 더하기 사이클
N = input()
if int(N) < 10: N = str(N)+'0'
temp = list(N)
ans = 1

while True:
    sum_num = int(temp[0]) + int(temp[1])
    sum_num = list(str(sum_num))
    if int(N) == int(temp[-1]+sum_num[-1]): break
    
    temp[0] = temp[-1]
    temp[1] = sum_num[-1]

    ans += 1

print(ans)   

# print(temp[-1], sum_num[-1], int(N), int(temp[-1]+sum_num[-1]))
"""

"""