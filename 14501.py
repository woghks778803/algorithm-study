# 실버3
# 퇴사
# 퇴사 디데이 입력
dday = int(input())
scheduler_list = []
max_benifit = 0

# 최대이익 계산 알고리즘
def benifit(scheduler_info, index, progress_date, work_dday, return_money):

    # 분기처리
    if work_dday > 0:
        # 이미 진행중인 일이 있는경우
        pass
    elif scheduler_info[0] - (dday-progress_date) > 1: 
        # 처리일자가 남은일자보다 큰 경우 - 무시
        pass
    else :
        # 처리일자가 남은일자보다 같거나 큰 경우 - 실행
        work_dday = scheduler_info[0]
        return_money += scheduler_info[1]

    if dday-progress_date < 1:   # 마지막날
        global max_benifit
        if max_benifit < return_money:
            max_benifit = return_money
        return True

    for j in range(index+1, len(scheduler_list)):
        progress_date += 1
        work_dday = work_dday-1
        benifit(scheduler_list[j], j, progress_date, work_dday, return_money)

# 퇴사까지 남은 일자별 
# 업무 처리 소요일, 이익금액 입력 및 저장
for i in range(0, dday):
    scheduler_list.append( list(map(int, input().split())) )

# 업무처리 진행 여부
work_chk = False
# 남은 업무처리일
work_dday = 0
# 진행일
progress_date = 0
for j in range(0, len(scheduler_list)):
    progress_date += 1
    benifit(scheduler_list[j], j, progress_date, work_dday, 0)

print(max_benifit)

# print(scheduler_list)
# print("실행할 업무 내용- : ",scheduler_info)
# print("실행일자 번호 : ",index)
# print("남은 날짜 : ",dday-progress_date, dday <= progress_date, progress_date, dday)
# print("남은 업무처리일 : ",work_dday)
# print("이익금 : ", return_money)
    
# 5
# 3 50