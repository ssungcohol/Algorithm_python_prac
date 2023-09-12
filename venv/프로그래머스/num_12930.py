
def solution(s):
    answer = ''

    words = s.split(" ")
    result = []

    for word in words:
        new_word = ""

        cnt = 0
        for i in range(len(word)):
            if (i == " "):
                new_word += " "
                cnt = 0
            elif (i % 2 == 0):
                new_word += word[i].upper()
                cnt += 1
            elif (i % 2 != 0):
                new_word += word[i].lower()
                cnt += 1
        result.append(new_word)

    answer = " ".join(result)

    print(answer)

solution("try hello world")