def solution(cacheSize, cities):
    answer = 0
    arr = []
    
    for city in cities:
        city = city.lower() # 모두 소문자로 만들기
        if city in arr:
            arr.remove(city) # 기존 위치에서 삭제
            answer += 1
        else:
            answer += 5
        arr.insert(0, city) # 제일 처음 위치에 넣는다.

        if len(arr) > cacheSize:
            arr.pop(len(arr) - 1) # 맨 마지막 위치의 city 삭제
    return answer