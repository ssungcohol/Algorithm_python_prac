
def solution(arr):
    answer = 0

    sum = 0
    for i in arr:
        sum += i

    answer = sum / len(arr)

    print(answer)

solution([1, 2, 3, 4])