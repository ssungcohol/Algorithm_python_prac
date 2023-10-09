
def solution(k, m, score):
    answer = 0

    score.sort()

    print(score)

    for i in range(len(score) - 1, -1, -1):
        if (len(score) - i) % m == 0:
            answer += score[i] * m

    print(answer)

solution(4, 3, [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2])