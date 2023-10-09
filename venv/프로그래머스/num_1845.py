
def solution(nums):
    answer = 0

    can = len(nums) // 2
    p_list = []

    for i in nums:
        if i not in p_list:
            p_list.append(i)

    if can == len(p_list) or can <= len(p_list):
        answer = can
    else:
        answer = len(p_list)


    print(answer)

solution([3,3,3,2,2,4])