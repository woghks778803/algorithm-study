# 쉽게 푸는 문제
# 실버5
A, B = map(int, input().split())
DP = [0]

cnt = 0
num = 1
while cnt < 1000:
    for i in range(num):
        DP.append(num)
        cnt += 1
    
    num += 1

print(sum(DP[A:B+1]))
# print(DP[A:B+1])