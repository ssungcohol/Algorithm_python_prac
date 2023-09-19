
def solution(s):
    answer = ''

    words = s.split(" ")

    # for i in range(len(words)):
    #
    #     if(words[i][0] == " "):
    #         answer += " "
    #     else:
    #         answer += words[i][0:1].upper()
    #         answer += words[i][1:].lower()
    #         answer += " "

    #========================================

    for i in range(len(words)):
        words[i] = words[i].capitalize()

    answer = " ".join(words)

    print(answer)

solution("3people unFollowed me")