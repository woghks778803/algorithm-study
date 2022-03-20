# 실버4
# 숫자놀이
def replace_solve(n):
    s = dic[n]
    return s

def solve(lst):
    for i in lst:
        lst_str = list(str(i))
        lst_str = " ".join( list(map(replace_solve, lst_str)) )
        result.append([lst_str, i])
    result.sort(key= lambda x : x[0])

    return result

if __name__ == "__main__":
    M, N  = map(int, input().split())
    dic = {'0':"zero", '1':"one", '2':"two", '3':"three", '4':"four", '5':"five", '6':"six", '7':"seven", '8':"eight", '9':"nine"}
    result = []

    T = [i for i in range(M, N+1)]
    result = solve(T)

    cnt = 0
    for i in result:
        cnt += 1

        if cnt%10 == 0: print(i[1])
        else: print(i[1], end=" ")

"""
8 28
"""