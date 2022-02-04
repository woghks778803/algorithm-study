# 실버2
# 부등호
def recursive(num_arr, cnt):
    for i in arr:
        if not visited[i]: 
            visited[i] = True
            temp_arr = num_arr.copy()
            temp_arr.append(i)

            if N+1 > cnt:
                recursive(temp_arr, cnt+1)
            else:
                if num_check(temp_arr): 
                    standard = int(''.join(map(str,temp_arr)))
                    global MAX
                    global MIN
                    MAX = max(MAX, standard)
                    MIN = min(MIN, standard)

            visited[i] = False

def num_check(num_lst):
    for i in range(N):
        if (T[i] == '>' and num_lst[i] < num_lst[i+1]) \
            or (T[i] == '<' and num_lst[i] > num_lst[i+1]):
            return False
    
    return True

if __name__ == "__main__":
    N = int(input())
    T = [i for i in input().split()]
    result = []
    MAX = 0
    MIN = 10000000000
    arr = [i for i in range(10)]
    visited = [False for i in range(10)]
    
    recursive([], 1)
    
    print(MAX)
    MIN = str(MIN)
    if len(MIN) <= N : print('0'+MIN)
    else: print(MIN)


"""
2
< >
9
> < < < > > > < <
"""