from sys import stdin as s

while True:
    nums = list(map(int, s.readline().rstrip().split()))
    if sum(nums) == 0:
        break;

    max_num = max(nums)
    nums.remove(max_num)
    if nums[0]**2 + nums[1]**2 == max_num**2: # 피타고라스 정리
        print('right')
    else:
        print('wrong')