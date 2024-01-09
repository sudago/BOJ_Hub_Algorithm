# 처음에 바로 로직을 못짰지만 그래도 딕셔너리, 투포인터 사용을 떠올렸다는걸 칭찬한다.
from collections import defaultdict

def solution(gems):
    dict = defaultdict(int)
    types = set(gems)
    type_count = 0
    lp, rp = 0, 0 # 왼쪽 포인터, 오른쪽 포인터
    answer = [1, len(gems)]

    while lp < len(gems) and rp <= len(gems): # 인덱스를 초과하지 않을 때 까지
        if type_count < len(types): # 모든 종류를 다 담지 않았다면
            if (rp == len(gems)): # 범위를 초과했다면
                break
            gem = gems[rp]
            if dict[gem] == 0: # 아직 담기지 않은 종류라면
                type_count += 1 # 담긴 종류 수를 상승 시킨다.
            dict[gem] += 1 # 갯수를 추가한다.
            rp += 1
        else: # 모든 종류가 다 담겼다면
            # 중복 보석 삭제해서 최소 값 구하기
            while lp <= rp:
                gem = gems[lp]
                # 현재 보석 제거하기
                dict[gem] -= 1
                lp += 1
                if dict[gem] == 0: # 보석 종류가 담겨있지 않다면
                    # 정답(=최소 값) 갱신하기.
                    answer_length = answer[1] - answer[0]
                    current_length = rp - lp
                    if (current_length < answer_length): # 최소 길이 갱신
                        answer = [lp, rp]
                    type_count -= 1 # 담긴 종류 수를 하락 시킨다.
                    break

    return answer
