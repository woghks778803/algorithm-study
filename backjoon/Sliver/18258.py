# 실버4
# 큐 2
import sys
import collections
N = int(sys.stdin.readline())
deq = collections.deque()

for i in range(N):
    command = sys.stdin.readline().split()
    
    if command[0] == "push":
        deq.append(command[1])
    elif command[0] == "pop":
        if len(deq) == 0: print(-1)
        else: print(deq.popleft())
    elif command[0] == "empty":
        if len(deq) == 0: print(1)
        else: print(0)
    elif command[0] == "size": 
        print(len(deq))
    elif command[0] == "front":
        if len(deq) == 0: print(-1)
        else:
            temp_num = deq.popleft()
            deq.appendleft(temp_num)
            print(temp_num)
    elif command[0] == "back":
        if len(deq) == 0: print(-1)
        else:
            temp_num = deq.pop()
            deq.append(temp_num)
            print(temp_num)

"""
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
"""