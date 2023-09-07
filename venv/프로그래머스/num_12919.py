
def solution(seoul):
    answer = ''

    for i in seoul:
        if(i == 'Kim'):
            answer = '김서방은 ' + str(seoul.index("Kim")) + '에 있다'

    print(answer)

solution(["Jane", "Kim"])