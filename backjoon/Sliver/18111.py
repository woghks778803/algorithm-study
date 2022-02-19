# 실버2
# 마인크래프트
if __name__ == "__main__":
    N, M, B = map(int, input().split())
    ground = [list(map(int, input().split())) for _ in range(N)]
    height_dict = dict()
    result = [1000000000, 0]
    for i in range(N):
        for j in range(M):
            if ground[i][j] not in height_dict:
                height_dict[ground[i][j]] = 0
            height_dict[ground[i][j]] += 1

    for h in range(min(height_dict), max(height_dict)+1):
        block = B
        time = 0
        for k, v in height_dict.items():
            if k < h:
                time += (h-k)*v
                block -= (h-k)*v
            else:
                time += (k-h)*2*v
                block += (k-h)*v
        if block < 0:
            break
        if time <= result[0]:
            result = time, h
    print(*result)
    
"""
3 4 99
0 0 0 0
0 0 0 0
0 0 0 1

3 4 1
64 64 64 64
64 64 64 64
64 64 64 63
"""