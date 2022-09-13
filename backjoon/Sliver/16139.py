# 실버1
# 인간-컴퓨터 상호작용
import sys
input = sys.stdin.readline
output = sys.stdout.write

S = list(input().strip())
DP = [[0 for _ in range(len(S))] for _ in range(26)]

for i in range(26):
    for j in range(len(S)):
        if ord(S[j])-97==i: DP[i][j] = DP[i][j-1] + 1
        else: DP[i][j] = DP[i][j-1]

q = int(input())

for _ in range(q):
    a, l, r = map(str, input().split())
    l = int(l)
    r = int(r)

    if l==0:
        output(str(DP[ord(a)-97][r])+"\n")
    else:
        output(str(DP[ord(a)-97][r] - DP[ord(a)-97][l-1])+"\n")
    
    


"""
seungjaehwang
4
a 0 5
a 0 6
a 6 10
a 7 10
"""