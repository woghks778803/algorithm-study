# 실버3
# 1로 만들기
N = int(input())

arr = []
arr.append(0)
arr.append(0)
arr.append(1)
arr.append(1)

for i in range(4, N+1):
    a = 1000001
    b = 1000001
    c = 1000001
    if i % 2 == 0:
        a = arr[i//2] + 1
    if i % 3 == 0:
        b = arr[i//3] + 1
    c = arr[i-1] + 1
    arr.append(min(a,b,c))

print(arr[N])
