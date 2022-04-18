# 브론즈3
# A+B - 4
# 테스트케이스 무중단 처리
# 답1
import sys
arr = sys.stdin.readlines()
for str in arr:
    a, b = map(int, str.strip().split())
    print(a+b)

# 답2
while True:
    try:
        N, M = map(int, input().split())
        print(N+M)
    except:
        break
    
"""
1 1
2 3
3 4
9 8
5 2
"""