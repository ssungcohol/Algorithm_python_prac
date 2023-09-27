
def solution(k, tangerine):
    answer = 0

    check = {}

    for i in tangerine:
        if i in check:
            check[i] += 1
        else:
            check[i] = 1

    check = dict(sorted(check.items(), key=lambda x: x[1], reverse=True))
    for i in check:
        if k <= 0:
            answer = answer
        else:
            k -= check[i]
            answer += 1

    print(answer)

solution(6, [1, 3, 2, 5, 4, 5, 2, 3])