
def solution(s):
    answer = []

    z_cnt = 0
    repeat = 0

    while (len(s) > 0):
        z_cnt += s.count("0")
        s = s.replace("0", "")
        s = format(len(s), 'b')
        repeat += 1
        if (len(s) == 1):
            answer.append(repeat)
            answer.append(z_cnt)
            break

    print(answer)

solution("110010101001")