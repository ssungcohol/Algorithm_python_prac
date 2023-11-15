
def solution(numbers, k):

    answer = numbers[2 * (k - 1) % len(numbers)]

    print(answer)

solution([1, 2, 3, 4], 2)