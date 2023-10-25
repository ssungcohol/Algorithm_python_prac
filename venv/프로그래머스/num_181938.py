
def solution(a, b):
    answer = 0

    re1 = str(a) + str(b)
    re2 = 2 * a * b

    if int(re1) > re2:
        answer = int(re1)
    elif int(re1) < re2:
        answer = re2
    elif int(re1) == re2:
        answer = int(re1)

    print(answer)

solution(2, 91)