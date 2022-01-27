# 실버3
# 예산
def binary_search(min_num, max_num):

    while max_num>=min_num:
        cost = (min_num+max_num)//2
        
        sum_num = 0
        for i in T:
            if i < cost: sum_num += i
            else: sum_num += cost

        if sum_num > M: max_num = cost-1
        else: min_num = cost+1

    return min_num-1
            

if __name__ == "__main__":
    N = int(input())
    T = [int(i) for i in input().split()]
    M = int(input())

    min_num = 0
    max_num = max(T)

    if sum(T) <= M:
        print(max_num)
    else:
        if min(T)*N <= M: min_num = min(T)
        print(binary_search(min_num, max_num))



    

    


"""
4
120 110 140 150
485

4
100 110 120 130
380

5
70 80 30 40 100
450
"""