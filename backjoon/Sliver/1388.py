# 실버4
# 바닥 장식
def dfs(x, y):
    if T[x][y] == "-":
        for m in move:
            next_point = y+m
            if M > next_point >= 0 and not visited[i][next_point] and T[x][y] == T[i][next_point]:
                visited[i][next_point] = True
                dfs(i, next_point)
    elif T[x][y] == "|":
        for m in move:
            next_point = x+m
            if N > next_point >= 0 and not visited[next_point][j] and T[x][y] == T[next_point][j]: 
                visited[next_point][j] = True
                dfs(next_point, j)

if __name__ == "__main__":
    N, M = map(int, input().split())

    T = [list(input()) for _ in range(N)]
    visited = [[False for _ in range(M)] for _ in range(N)]
    move = [1, -1]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if not visited[i][j]:
                cnt += 1
                visited[i][j] = True
                dfs(i, j)

    print(cnt)
    print(T)


"""
4 4
----
----
----
----

6 9
-||--||--
--||--||-
|--||--||
||--||--|
-||--||--
--||--||-

7 8
--------
|------|
||----||
|||--|||
||----||
|------|
--------

6 6
-||--|
||||||
|||-|-
-||||-
||||-|
||-||-
"""