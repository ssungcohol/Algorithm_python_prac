
#자릿수 더하기

def solution(n):
    answer = 0

    for i in str(n):
        answer += int(i)

    print(answer)

solution(1234)