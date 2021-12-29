# 브론즈3
# 배수와 약수
if __name__ == "__main__":
    
    while True:
        N, M = map(int, input().split())
        if N == 0 and M == 0:
            break
        elif M % N == 0:
            print("factor")
        elif N % M == 0:
            print("multiple")
        else:
            print("neither")
        
"""
8 16
32 4
17 5
0 0
"""