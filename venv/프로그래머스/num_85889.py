
def solution(babbling):

    answer = 0

    speak = ['aya', 'ye', 'woo', 'ma']

    for i in babbling:
        for s in speak:
            i = i.replace(s, ' ')
        i = i.replace(' ', '')
        if len(i) == 0:
            answer += 1

    print(answer)


solution(["aya", "yee", "u", "maa", "wyeoo"])