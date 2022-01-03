# 실버4
# 별 찍기 - 19
import sys
N = int(input())
star_len = 1 + (4 * (N-1))

for i in range(star_len):
    if i % 2 == 0:
        for j in range(star_len):
            if star_len//2 >= i: # 중간보다 위에 있을경우
                if not (i <= j < star_len-i or j%2 == 0): sys.stdout.write(" ")
                else: sys.stdout.write("*")
            else: # 중간보다 아래 위치
                if not (star_len-i-1 <= j <= i or j%2 == 0): sys.stdout.write(" ")
                else: sys.stdout.write("*")
    else:
        for j in range(star_len): # 1~7, 3~5
            if star_len//2 >= i:
                if i <= j < star_len-i or j%2 != 0: sys.stdout.write(" ")
                else: sys.stdout.write("*")
            else:
                if star_len-i-1 <= j <= i or j%2 != 0: sys.stdout.write(" ")
                else: sys.stdout.write("*")
    
    sys.stdout.write("\n")
