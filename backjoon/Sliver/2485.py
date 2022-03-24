# 실버4
# 가로수
import sys
input = sys.stdin.readline
N = int(input())
T = [int(input()) for _ in range(N)]
diff = [T[i]-T[i-1] for i in range(1, N)]

a = diff[0]
b = diff[1]
while True:
    if a%b == 0: break
    temp = b
    b = a%b
    a = temp

for i in range(2, N-1):
    a = diff[i]

    while True:
        if a%b == 0: break
        temp = b
        b = a%b
        a = temp

all = (T[-1]-T[0]) // b+1
print(all-N)

"""
4
1
3
7
13
"""