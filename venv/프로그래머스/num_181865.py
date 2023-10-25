
def solution(binomial):
    answer = 0

    ex = binomial.split(' ')

    if ex[1] == '+':
        answer = int(ex[0]) + int(ex[2])
    elif ex[1] == '-':
        answer = int(ex[0]) - int(ex[2])
    else:
        answer = int(ex[0]) * int(ex[2])

    print(answer)

solution("43 + 12")