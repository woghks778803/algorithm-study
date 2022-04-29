# 실버4
# 숫자야구
def create_arr():
    arr = [True for _ in range(1000)]

    #각 자리가 서로 다른 숫자여야 하는데 같은 숫자거나 0이 포함된 수는 False로 설정합니다.
    for i in range(123, 1000):
        l = str(i)
        if l[0]==l[1] or l[1]==l[2] or l[0]==l[2]:
            arr[i] = False

        if '0' in l:
            arr[i] = False

    return arr

def solve():
    arr = create_arr()
    N = int(input())

    for _ in range(N):
        v, s, b = map(int, input().split())

        for j in range(123, 1000):
            if not arr[j]: continue

            #세자리 수들을 입력받은 수랑 비교하여 스트라이크 개수와 볼 개수를 셉니다.
            s_cnt = 0
            b_cnt = 0

            for x in range(0, 3):
                for y in range(0, 3):
                    if str(v)[x]==str(j)[y]:
                        if x==y: s_cnt += 1
                        else: b_cnt += 1

            #구한 스트라이크 개수와 볼 개수가 입력받은 개수들이랑 다를경우 False로 처리합니다.
            if s!=s_cnt or b!=b_cnt:
                arr[j] = False
        
    #세자리 수 중에서 True인 개수를 출력합니다.
    print(arr[123:1000].count(True))

    # for i in range(123, 1000):
    #     if arr[i]: print(i)

if __name__ == "__main__":
    solve()



"""
4
123 1 1
356 1 0
327 2 0
489 0 1
"""