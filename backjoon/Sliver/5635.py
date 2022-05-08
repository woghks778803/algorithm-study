# 실버5
# 생일
def data_conversion(val):
    try:
        data = int(val)
    except ValueError as e:
        data = val

    return data

N = int(input())
T = [list(map(data_conversion, input().split())) for _ in range(N)]
T.sort(key= lambda x : (x[3], x[2], x[1]))

print(T[-1][0])
print(T[0][0])



"""
5
Mickey 1 10 1991
Alice 30 12 1990
Tom 15 8 1993
Jerry 18 9 1990
Garfield 20 9 1990
"""