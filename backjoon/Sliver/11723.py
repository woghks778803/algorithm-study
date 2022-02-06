# 실버5
# 집합
if __name__ == "__main__":
    import sys
    input = sys.stdin.readline
    output = sys.stdout.write
    M = int(input())
    S = 0
    for i in range(M):
        command = input().split()
        op = command[0]
        if len(command) == 2: elem = int(command[1])
        if op == "add":
            S |= 1<<elem
        elif op == "remove":
            S &= ~(1<<elem)
        elif op == "check":
            if S & (1<<elem) == 0: output("0\n")
            else: output("1\n")
        elif op == "toggle":
            S ^= 1<<elem
        elif op == "all":
            S = (1<<21) - 1
        elif op == "empty":
            S = 0

"""
26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1
"""
