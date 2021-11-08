# 실버2
# 신나는 함수 실행
def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    elif a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    elif arr[a][b][c] != 0: 
        return arr[a][b][c]
    elif a < b and b < c:
        arr[a][b][c-1] = w(a, b, c-1)
        arr[a][b-1][c-1] = w(a, b-1, c-1)
        arr[a][b-1][c] = w(a, b-1, c)
        return arr[a][b][c-1] + arr[a][b-1][c-1] - arr[a][b-1][c]
        # arr[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        # return arr[a][b][c]
        # return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        arr[a-1][b][c] = w(a-1, b, c)
        arr[a-1][b-1][c] = w(a-1, b-1, c)
        arr[a-1][b][c-1] = w(a-1, b, c-1)
        arr[a-1][b-1][c-1] = w(a-1, b-1, c-1)
        return arr[a-1][b][c] + arr[a-1][b-1][c] + arr[a-1][b][c-1] - arr[a-1][b-1][c-1]
        # arr[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        # return arr[a][b][c]
        # return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)

arr = [[[0 for i in range(50)] for j in range(50)] for k in range(50)]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    else:
       print("w({0}, {1}, {2}) =".format(a,b,c), w(a,b,c))

"""
1 1 1
2 2 2
10 4 6
50 50 50
-1 7 18
-1 -1 -1
"""