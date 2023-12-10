from collections import deque

def solution(queue1, queue2):
    answer = 0
    limit = (len(queue1) + len(queue2)) * 2
    q1 = deque()
    q2 = deque()
    sum_q1 = 0
    sum_q2 = 0
    for i in range(len(queue1)):
        e = queue1[i]
        q1.append([e, i]) # 원소, 인덱스 저장
        sum_q1 += e
    for i in range((len(queue2))):
        e = queue2[i]
        q2.append([e, i]) # 원소, 인덱스 저장
        sum_q2 += e
    if ((sum_q1 + sum_q2) % 2 != 0): # 홀수라면
        return -1
    
    while True:
        if answer >= limit: # 최대 이동 횟수
            return -1
        if sum_q1 == sum_q2: # 기저 조건 (base case)
            return answer
        elif sum_q1 > sum_q2:
            e = q1.popleft()
            q2.append(e)
            sum_q1 -= e[0] # 값
            sum_q2 += e[0]
        else: # sum_q1 < sum_q2
            e = q2.popleft()
            q1.append(e)
            sum_q1 += e[0]
            sum_q2 -= e[0]
        
        if q1[0][1] == 0 and q2[0][1] == 0: # 각 큐가 원상복구되면
            return -1
        answer += 1 # count++
    
    return answer