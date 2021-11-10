# 실버2
# 하노이 탑 이동 순서
# X
N = int(input())
arr = [1]
for i in range(N-1):
    arr.append((arr[i]*2)+1)
print(max(arr))

def recursion(m, a, b):
    if m:
        recursion(m-1, a, 6-a-b)
        print(a,b)
        recursion(m-1, 6-a-b, b)

recursion(N, 1, 3)

'''
반례

입력값
3

출력값
7 
1 3
1 2
3 2
1 3
2 1
2 3
1 3
'''
