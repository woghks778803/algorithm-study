# 실버4
# 에어컨
N, K = map(int, input().split())
chk = [1080, 180, 180] # 1, 2, 3번째 시간주기

arr = []
DAY = 1440
result = -180

# 에어컨 꺼지는 시간 저장
while (N*DAY)+DAY > result:

    for c in range(3):
        result += chk[c]
        if N*DAY <= result < (N*DAY)+DAY:
            arr.append(result%1440)

        if c==2: result += K

# 시간계산 및 출력
print(len(arr))      
for a in arr:
    h = a//60
    m = a%60

    if h<10: h = "0"+str(h)
    if m<10: m = "0"+str(m)

    print(f"{h}:{m}")

"""
1000 59
"""