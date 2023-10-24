
def solution(arr, delete_list):
    answer = []

    for i in arr:
        if i not in delete_list:
            answer.append(i)

    print(answer)

solution([293, 1000, 395, 678, 94], [94, 777, 104, 1000, 1, 12])