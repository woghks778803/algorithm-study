# 실버2
# 유기농 배추
import sys
import copy
sys.setrecursionlimit(10**6) # 백준 런타임에러
N = int(input())

def pointCheck(cx, cy, x, y, checkmap, loadmap):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    for i in range(len(dx)):
        if cx+dx[i] >= 0 and cx+dx[i] < x and cy+dy[i] >= 0 and cy+dy[i] < y: # 좌표 범위에 속할떄
            if checkmap[cy+dy[i]][cx+dx[i]] == False and loadmap[cy+dy[i]][cx+dx[i]] == True: # 검사가 안된 지역이고 배추가 심어져있는 지역인 경우
                checkmap[cy+dy[i]][cx+dx[i]] = True
                pointCheck(cx+dx[i], cy+dy[i], x, y, checkmap, loadmap)
            

for i in range(N):
    test_case = list(map(int, sys.stdin.readline().split()))
    x = test_case[0]
    y = test_case[1]
    
    input_list = []
    checkmap = []
    loadmap = []
    for j in range(y):
        checkmap.append([False for n in range(x)])
    loadmap = copy.deepcopy(checkmap)

    for k in range(test_case[2]):
        input_point = tuple(map(int, input().split()))
        loadmap[input_point[1]][input_point[0]] = True
        input_list.append(input_point)
    
    bug_cnt = 0
    for cy in range(y):
        for cx in range(x):
            if checkmap[cy][cx] == True or loadmap[cy][cx] == False: # 이미 체크했거나 배추를 심지않은곳
                continue
            else:
                bug_cnt += 1
                checkmap[cy][cx] = True
                # 주변 영역 체크
                pointCheck(cx, cy, x, y, checkmap, loadmap)
    print(bug_cnt)
    # print("bug_cnt : ",bug_cnt)
    # print(loadmap)
    # print(checkmap)
    # print(input_list)
