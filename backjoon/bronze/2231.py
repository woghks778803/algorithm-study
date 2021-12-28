# 브론즈2
# 분해합
def decomposeSum(n):
    for i in range(n):
        sum_num = i
        for add_num in map(int, str(i)):
            sum_num += add_num
        
        if sum_num == n: 
            ans.append(i)
            return i     
    
    if not ans: return 0

if __name__ == "__main__":
    N = int(input())
    ans = []
    print(decomposeSum(N))