# 브론즈5
# 0 = not cute / 1 = cute
n = int(input())

if (n >= 1 and n <= 101) and n%2==1 :
    y_cnt = 0
    n_cnt = 0

    for i in range(0, n):
        answer = int(input())

        if answer == 1:
            y_cnt += 1
        else:
            n_cnt += 1

    if y_cnt > n_cnt:
        print("Junhee is cute!")
    else:
        print("Junhee is not cute!")