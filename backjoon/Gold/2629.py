# 골드3
# 양팔저울
# X
N = int(input())
plumb = [int(i) for i in input().split()]
M = int(input())
marbles = [int(i) for i in input().split()]
DP = [[0 for _ in range((i+1)*500+1)] for i in range(N+1)]

def calc(num, weight):
    if num > N: return
    if DP[num][weight]: return

    DP[num][weight] = 1
    calc( num+1, weight )
    calc( num+1, weight+plumb[num-1] )
    calc( num+1, abs(weight-plumb[num-1]) )
    
calc(0, 0)

result = []
for i in marbles:
    if i > 30*500:
        result.append("N")
        continue
    if DP[N][i] == 1:
        result.append("Y")
    else:
        result.append("N")

print(*result)
"""
2
1 4
2
3 2

4
2 3 3 3
3
1 4 10
"""