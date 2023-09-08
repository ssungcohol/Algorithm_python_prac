
def solution(arr, divisor):
    answer = []

    for i in arr:
        if (i % divisor == 0):
            answer.append(i)

    answer.sort()

    if (len(answer) > 0):
        print(answer)
    else:
        answer.append(-1)
        print(answer)

solution([2, 36, 1, 3], 1)