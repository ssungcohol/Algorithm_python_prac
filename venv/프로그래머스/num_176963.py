
def solution(name, yearning, photo):

    answer = []

    for i in photo:
        score = 0
        for j in i:
            if j in name:
                score += yearning[name.index(j)]
        answer.append(score)

    print(answer)

solution(["kali", "mari", "don"], [11, 1, 55],
         [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]])