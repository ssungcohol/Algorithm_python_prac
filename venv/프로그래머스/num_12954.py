
def solution(x, n):

    answer = []

    for i in range(1, n + 1):
        answer.append(i*x)

    print(answer)

solution(4, 3)