# 실버4
# 스택 
command_cnt = int(input())
command_list = []
stack = []

# 입력된 명령어 저장
for i in range(0, command_cnt):
    command_list.append(list(map(str, input().split())))

for info in command_list:
    # 명령어 처리
    if info[0] == "push": stack.append(int(info[1]))
    elif info[0] == "pop":
        if len(stack) == 0: print(-1)
        else:
            print(stack[len(stack)-1])
            del stack[len(stack)-1]
    elif info[0] == "size": print(len(stack))
    elif info[0] == "empty":
        if len(stack) == 0: print(1)
        else: print(0)
    elif info[0] == "top":
        if len(stack) == 0: print(-1)
        else: print(stack[len(stack)-1])