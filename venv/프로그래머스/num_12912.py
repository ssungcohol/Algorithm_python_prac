
def solution(x, y):
    answer = 0

    if (x > y):
        for i in range(y, x + 1):
            answer += i
    elif (x < y):
        for i in range(x, y + 1):
            answer += i
    elif (x == y):
        answer = x

    print(answer)

solution(3, 5)