
def solution(answers):
    answer = []

    num_1 = [1, 2, 3, 4, 5]
    num_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]

    #점수 확인
    for i in range(len(answers)):
        if answers[i] == num_1[i % 5]:
            score[0] += 1
        if answers[i] == num_2[i % 8]:
            score[1] += 1
        if answers[i] == num_3[i % 10]:
            score[2] += 1

    score_max = max(score)
    #최대 점수 추출

    for i in range(len(score)):
        if score_max == score[i]:
            answer.append(i + 1)

    print(answer)

solution([1,3,2,4,2])