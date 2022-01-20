# 골드4
# 전화번호 목록
import sys
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    arr = [input().strip() for _ in range(N)]
    arr.sort()
    for i in range(N-1):
        if arr[i] == arr[i+1][0:len(arr[i])]:
            print("NO")
            break
    else:
        print("YES")

"""
2
3
911
97625999
91125426
5
113
12340
123440
12345
98346
"""