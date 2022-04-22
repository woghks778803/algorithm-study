# 실버3
# 무한이진트리
def dfs(a, b):
    if a == 1:
        result[1] += b-1
        return 0
    
    if b == 1:
        result[0] += a-1
        return 0
    
    if a < b:
        result[1] += b//a
        dfs(a, b%a)

    if a > b:
        result[0] += a//b
        dfs(a%b, b)
        

A, B = map(int, input().split())
result = [0,0]
dfs(A, B)

print(*result)