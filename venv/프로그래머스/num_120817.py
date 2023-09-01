
# 배열의 평균값

def solution(numbers) :

    sum = 0

    for num in numbers :
        sum += num

    result = sum / len(numbers)
    print(result)

solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])