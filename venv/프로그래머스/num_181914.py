
def solution(number):
    answer = 0

    rest = 0
    for i in number:
        rest += int(i)

    answer = rest % 9

    print(answer)

solution("123")