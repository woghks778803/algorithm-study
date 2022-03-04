# 골드4
# 크게 만들기
# 투 포인터
N, K = map(int, input().split())
temp_k = K
number = input()
result = []
for i in range(N):
    while K > 0 and result:
        if result[-1] < number[i]:
            K -= 1
            result.pop()
        else:
            break

    result.append(number[i])

for i in range(N-temp_k): print(result[i], end="")
# print(''.join(result))

"""
7 3
1231234

7 3
1031030

10 4
4177252841

10 5
4177252841
"""