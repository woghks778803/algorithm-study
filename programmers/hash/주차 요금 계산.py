def solution(fees, records):
    import math
    answer = []
    tp = ['IN', 'OUT']
    use_number_time = {}
    in_number_time = {}
    arr = []
    
    for i in records:
        time, number, input_tp = i.split()
        hour, minute = map(int, time.split(":"))
        
        if input_tp == tp[0]: # 입차
            if hour == 23 and minute == 59:
                pass
            else:
                in_number_time[number] = hour*60 + minute
                
        else: # 출차
            if use_number_time.get(number): use_number_time[number] += (hour*60 + minute) - in_number_time[number]
            else: use_number_time[number] = (hour*60 + minute) - in_number_time[number]
            in_number_time[number] = None
    
    # 마지막 출차
    for number in in_number_time:
        if in_number_time[number] != None:
            if use_number_time.get(number): use_number_time[number] += 23*60 + 59 - in_number_time[number]
            else: use_number_time[number] = 23*60 + 59 - in_number_time[number]
            in_number_time[number] = None
        arr.append([number, use_number_time[number]])
        
    arr.sort()
    
    for i in arr:
        if i[1] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((i[1] - fees[0]) / fees[2]) * fees[3])
            
    return answer