
def solution(numbers):
    answer = 45

    for i in numbers:
        answer -= i

    print(answer)

solution([1,2,3,4,6,7,8,0])