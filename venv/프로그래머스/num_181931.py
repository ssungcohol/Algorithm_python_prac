
def solution(a, d, included):
    answer = 0

    answer = 0
    num = 0

    for i in range(len(included)):
        answer = a + (d * i)
        if included[i]:
            num += answer

    print(num)

solution(3, 4, [true, false, false, true, true])