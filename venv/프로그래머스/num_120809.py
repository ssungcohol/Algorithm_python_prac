
#배열 두 배 만들기

def solution(numbers):
    answer = []

    answer =[i*2 for i in numbers]

    print(answer)

solution([1, 2, 3, 4, 5])