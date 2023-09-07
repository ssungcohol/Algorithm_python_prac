import math


def solution(n):
    answer = 0

    sqrt = math.sqrt(n)
    check = int(sqrt)

    # print(math.pow(check + 1)) if (sqrt == check) else print(-1)

    if (sqrt == check):
        answer = (check + 1)**2
    else:
        answer = -1

    print(answer)

solution(3)