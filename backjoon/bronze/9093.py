# 브론즈1
# 단어 뒤집기
T = int(input())

for i in range(T):
    # 문장 입력받기
    input_strs = list(map(str, input().split()))

    # 역순 출력
    reverse_str = ""
    for input_str in input_strs:
        reverse_str += "".join(reversed(input_str)) + " "
    print(reverse_str)
        
"""
2
I am happy today
We want to win the first prize
"""