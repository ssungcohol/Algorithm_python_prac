
def solution(money):

    answer = []

    answer.append(money // 5500)
    answer.append(money % 5500)

    print(answer)

solution(15000)