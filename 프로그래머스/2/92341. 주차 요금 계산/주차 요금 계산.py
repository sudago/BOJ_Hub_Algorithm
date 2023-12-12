from collections import defaultdict
import math

def solution(fees, records):
    # fee[0] 기본 시간. fee[1] 기본 요금, fee[2] 단위 시간, fee[3] 딘위 요금
    default_time, default_fee, unit_time, unit_fee = fees
    dict = defaultdict(list) # 번호판에 따라 [입차, 출차] 기록
    temp_list = []
    
    for record in records:
        time, car_num, in_out = record.split()
        if in_out == "IN": # 입차라면
            dict[car_num].append([time, 0])
        else: # 출차라면
            for times in dict[car_num]: # 입차 기록을 찾는다
                if times[1] == 0: # 출차 기록이 없으면 시간을 기록한다
                    times[1] = time
                    break
                    
    for car_num, time_records in dict.items():
        cumulative_time = 0 # 누적 시간
        for time_record in time_records:
            in_time, out_time = time_record
            in_hour, in_minute = map(int, in_time.split(":")) # 분으로 바꾸는 작업
            in_minutes = (in_hour * 60) + in_minute
            if (out_time == 0):
                out_time = "23:59"
            out_hour, out_minute = map(int, out_time.split(":"))
            out_minutes = (out_hour * 60) + out_minute
            cumulative_time += out_minutes - in_minutes # 누적 시간에 계속 더한다
        cumulative_time -= default_time # 기본 시간을 빼준다
        if cumulative_time < 0: # 기본 시간을 뺀 누적 시간이 음수라면 0으로 세팅
            cumulative_time = 0
        total_fee = default_fee + (math.ceil(cumulative_time / unit_time) * unit_fee) # 주차 요금 공식 적용
        temp_list.append([car_num, total_fee])
        
    temp_list.sort() # 차량 번호가 작은 순서대로 정렬
    answer = [fee for _ , fee in temp_list] # 주차 요금만 담아서 출력
        
    return answer