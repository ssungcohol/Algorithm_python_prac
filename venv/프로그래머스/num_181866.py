
def solution(myString):
    answer = []

    x_string = myString.split('x')

    for i in x_string:
        if len(i) > 0:
            answer.append(i)

    answer.sort()

    print(answer)

solution("axbxcxdx")