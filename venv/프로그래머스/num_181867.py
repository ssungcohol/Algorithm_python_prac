
def solution(myString):
    answer = []

    x_string = myString.split('x')

    for i in x_string:
        answer.append(len(i))

    print(answer)

solution("oxooxoxxox")