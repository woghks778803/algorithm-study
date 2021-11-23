# 실버4
# 덱
import sys
import collections
N = int(sys.stdin.readline())
deq = collections.deque()

for i in range(N):
    command = list(sys.stdin.readline().split())

    if command[0] == "push_front": deq.appendleft(command[1])
    elif command[0] == "push_back": deq.append(command[1])
    elif command[0] == "pop_front":
        if not deq: print(-1)
        else: print(deq.popleft())
    elif command[0] == "pop_back":
        if not deq: print(-1)
        else: print(deq.pop())
    elif command[0] == "size": print(len(deq))
    elif command[0] == "empty":
        if not deq: print(1)
        else: print(0)
    elif command[0] == "front":
        if not deq: print(-1)
        else: print(deq[0])
    elif command[0] == "back":
        if not deq: print(-1)
        else: print(deq[-1])
    
"""
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front

22
front
back
pop_front
pop_back
push_front 1
front
pop_back
push_back 2
back
pop_front
push_front 10
push_front 333
front
back
pop_back
pop_back
push_back 20
push_back 1234
front
back
pop_back
pop_back
"""