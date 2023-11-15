
def solution(s):
    answer = 0

    s1 = s.split()

    for i in range(len(s1)):
        if s1[i] == 'Z':
            answer -= int(s1[i - 1])
        else:
            answer += int(s1[i])

    print(answer)

solution("1 2 Z 3")