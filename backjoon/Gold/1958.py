# 골드3
# LCS 3
a = input()
b = input()
c = input()
x_len = len(a)+1
y_len = len(b)+1
z_len = len(c)+1

result = 0
LCS = [[[0 for _ in range(z_len)] for _ in range(y_len)] for _ in range(x_len)]

for i in range(1, x_len):
    for j in range(1, y_len):
        for k in range(1, z_len):
        
            if a[i-1] == b[j-1] == c[k-1]: 
                LCS[i][j][k] = LCS[i-1][j-1][k-1] + 1
            else:
                LCS[i][j][k] = max(LCS[i-1][j][k], LCS[i][j-1][k], LCS[i][j][k-1])

            if LCS[i][j][k] > result: result = LCS[i][j][k]
        
print(result)
# print(LCS)

"""
abcdefghijklmn
bdefg
efg

asfasga
sdhsdhsdf
gsdafs

daefc
aefc
daef

axbyc
aibjc
ambnc
"""