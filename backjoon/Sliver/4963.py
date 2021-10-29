# 실버2
# 섬의 개수
import sys
sys.setrecursionlimit(10**6) # 백준 런타임에러
def checkMap(i, j, loadmap, list_check):
    x = [-1, -1, -1, 0, 0, 1, 1, 1]
    y = [-1, 0, 1, -1, 1, -1, 0, 1]
    # 주변 섬 검사
    for k in range(len(x)):
        if i+x[k] >= 0 and i+x[k] < h and j+y[k] >= 0 and j+y[k] < w: # 지도 범위 안
            if loadmap[i+x[k]][j+y[k]] == 1 and list_check[i+x[k]][j+y[k]] == False: # 값이 1이면 같은 섬
                list_check[i+x[k]][j+y[k]] = True # 같은 섬이니 섬 카운트는 세지않고 범위만 저장
                checkMap(i+x[k], j+y[k], loadmap, list_check)

while True:
    w, h = list(map(int, sys.stdin.readline().split()))
    if w == 0 and h == 0:
        break

    loadmap = []
    list_check = []
    for i in range(h):
        loadmap.append( list(map(int, sys.stdin.readline().split())) )
        list_check.append([False for b in range(w)])
    # print(loadmap)
    # print(list_check)
    land_count = 0

    # 그래프 알고리즘
    for i in range(h):
        for j in range(w):
            if loadmap[i][j] == 1 and list_check[i][j] == False:
                # 현재 섬 영역 중 체크 내역에 포함되지않았는지 확인
                    # print(i, j, list_check[i][j])
                    list_check[i][j] = True
                    land_count += 1
                    checkMap(i, j, loadmap, list_check)

    print(land_count)
