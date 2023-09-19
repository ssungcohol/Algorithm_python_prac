
def solution(s):
    answer = 0

    check = []

    for i in s:
        check.append(i)
        if len(check) > 1 and check[-1] == check[-2]:
            check.pop()
            check.pop()

    if len(check) == 0:
        answer = 1
    else:
        answer = 0

    print(answer)

solution("baabaa")