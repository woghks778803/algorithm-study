# 실버1
# 신입 사원
T = int(input())
cnt = 0

while cnt < T:
    cnt += 1
    N = int(input())
    arr = []
    for i in range(N):
        arr.append(list(map(int, input().split())))
    
    arr.sort()
    result = 1
    target = arr[0][1]
    for i in arr[1:]:
        if target > i[1]:
            result += 1
            target = i[1]

    print(result)

"""
2
5
3 2
1 4
4 1
2 3
5 5
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
"""