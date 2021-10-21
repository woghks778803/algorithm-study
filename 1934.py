# 실5
# 최소공배수
test_case_cnt = int(input())
test_case_list = []

for i in range(test_case_cnt):
    num1, num2 = map(int, input().split())
    
    # 최대공약수 산출
    gcd = 1

    if num1<num2:
        temp=num1
        num1=num2
        num2=temp
    big=num1
    small=num2

    chk = False
    while num1%num2 != 0: 
        chk = True
        gcd=num1%num2
        num1=num2
        num2=gcd
    
    if chk == False:
        gcd = small

    # 최대공약수를 통한 최소공배수 계산
    print(int(big*small/gcd))

    # if min(num1, num2) == 1:
    #     gcd = min(num1, num2)
    # elif num1 == num2:
    #     gcd = num1
    # elif num1 > num2:
    #     for i in reversed(range(2, num2+1)):
    #         if num1 % i == 0 and num2 % i == 0:
    #             gcd = i
    #             break
    # elif num1 < num2:
    #     for i in reversed(range(2, num1+1)):
    #         if num1 % i == 0 and num2 % i == 0:
    #             gcd = i
    #             break
    
    


# 테스트 케이스별 최소공배수 산출
# for test_case in test_case_list:

# T=int(input())
# c=1
# for i in range(T):
#     a,b=map(int,input().split())
#     if b<a:
#         temp=b
#         b=a
#         a=temp
#     one=a
#     two=b

#     chk = False
#     while b%a != 0: 
#         chk = True
#         c=b%a
#         b=a
#         a=c
    
#     if chk == False:
#         c = one
#     print(int(one*two/c))

# print(test_case_list)