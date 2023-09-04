
#피자 나눠먹기(3)

def solution(slice, n):

    answer = 0
    if (n % slice > 0):
        answer = (n // slice) + 1
    else: answer = n // slice

    print(answer)

solution(4, 12)