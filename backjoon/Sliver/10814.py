# 실버5
# 나이순 정렬
n = int(input())
user_list = []

if n >= 1 and n <= 100000:
    for i in range(0,n):
        age, name = map(str, input().split())
        user_list.append( (int(age),i,name) )

    user_list.sort(key=lambda x : (x[0], x[1]))

    for user in user_list:
        print(user[0], user[2])

