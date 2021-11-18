# 브론즈1
# 분수찾기
X = int(input())

x = 1
y = 1
add_x = 0
add_y = 0
switch = False
count = 0

while True:
    count += 1
    X -= count
    if switch: 
        switch = False
        add_x = 1
        add_y = -1
        x = 1
        y = count
    else: 
        switch = True
        add_x = -1
        add_y = 1
        x = count
        y = 1
        
    if X <= 0:
        for i in range(abs(X)):
            x += add_x
            y += add_y
        print(str(y)+"/"+str(x))
        break
    