
#배열 뒤집기

def solution(num_list):

    # 방법1 - reverse() 함수 사용
    num_list.reverse()

    # 방법2 - 슬라이싱 사용 list[::1]
    num_list = num_list[::-1]

    # 방법3 - for문 사용
    for right in range(len(num_list) // 2):
        left = len(num_list) - right - 1
        temp = num_list[right]
        num_list[right] = num_list[left]
        num_list[left] = temp

    answer = num_list

    print(answer)

solution([1, 2, 3 ,4 ,5])