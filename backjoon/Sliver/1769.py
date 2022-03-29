# 실버5
# 3의 배수
X = input()

cnt = 0
while len(X) > 1:
    cnt += 1
    X = str(sum(map(int, list(X))))

print(cnt)
if int(X)%3==0:
    print("YES")
else:
    print("NO")

