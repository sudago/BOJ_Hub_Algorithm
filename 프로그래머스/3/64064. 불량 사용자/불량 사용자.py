from itertools import permutations

def check_permutations(banned_id, users):
    for i in range(len(banned_id)):
        if len(banned_id[i]) != len(users[i]): # 문자열 길이가 같지 않을 경우
            return False
        for j in range(len(banned_id[i])): 
            if banned_id[i][j] == '*': # *일 경우 스킵
                continue
            if banned_id[i][j] != users[i][j]: # *제외하고 두 문자열이 하나라도 일치하지 않으면
                return False
    return True

def solution(user_id, banned_id):
    user_permutation = list(permutations(user_id, len(banned_id))) # 순열 - 순서와 상관없이 조합
    ban_set = []
    for users in user_permutation:
        if check_permutations(banned_id, users):
            users = set(users) # user 순서와 관계 없이 판단하기 위함.
            if users not in ban_set:
                ban_set.append(users)

    return len(ban_set)
    