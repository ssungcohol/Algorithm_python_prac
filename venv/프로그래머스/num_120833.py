
#배열 자르기

def solution(numbers, num1, num2):
    answer = []

    answer = numbers[num1:num2+1]

    print(answer)

solution([1, 2, 3, 4, 5], 1, 3)