import math

def change_to_k_base(n, k):
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
    return rev_base[::-1]
    
def isPrime(num):
    if num <= 1:
        return False
    for i in range(3, math.floor(math.sqrt(num))+1): # 제곱근은 소수 -> 정수로 올림 -> 테스트 케이스 14, 16번 실패로 동등비교(+1) 추가
        if num % i == 0:
            return False
    return True
    
def solution(n, k):
    answer = 0
    k_base = change_to_k_base(int(n), int(k)) # n을 k 진수로 변환
    nums = k_base.split('0')
    for num in nums:
        if num == '': 
            continue
        answer += isPrime(int(num)) # 소수 파악 후 count
    
    return answer