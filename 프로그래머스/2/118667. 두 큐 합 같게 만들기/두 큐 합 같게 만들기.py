# 문제: https://school.programmers.co.kr/learn/courses/30/lessons/118667
# 테스트 케이스 11, 28번 시간 초과 -> limit 정해서 해결. 11번은 큰 배열인 듯.
# 테스트 케이스 1번 실패 -> limit을 넉넉하게 정해서 해결
# 좀 지저분한 코드인듯.. 투포인터로 푸는 것이 깔끔. https://school.programmers.co.kr/questions/37142
from collections import deque

def solution(queue1, queue2):
    answer = 0
    limit = (len(queue1) + len(queue2)) * 2
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum_q1 = sum(queue1)
    sum_q2 = sum(queue2)
    if ((sum_q1 + sum_q2) % 2 != 0): # 홀수라면, 현재 테스트 케이스에서는 필요없는 조건이지만 테스트케이스 추가 될 경우 필요.
        return -1
    
    while True:
        if answer >= limit: # 최대 이동 횟수, 1번 해결
            return -1
        if sum_q1 == sum_q2: # 기저 조건 (base case)
            return answer
        elif sum_q1 > sum_q2:
            e = q1.popleft()
            q2.append(e)
            sum_q1 -= e
            sum_q2 += e
        else: # sum_q1 < sum_q2
            e = q2.popleft()
            q1.append(e)
            sum_q1 += e
            sum_q2 -= e
        
        answer += 1 # count++
    
    return answer
    
# 테스트 케이스 11, 28 반례
# queue1 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 10], queue2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# 테스트 케이스 1번 반례
# queue1 = [3, 3, 3, 3], queue2 = [3, 3, 21, 3]

queue1 = [1, 1]
queue2 = [1, 5]
print(solution(queue1, queue2))
