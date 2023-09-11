
def solution(s):
    answer = True

    if (len(s)==4 or len(s)==6):
        for i in s:
            if(ord(i) >= 65 and ord(i) <= 122):
                answer = False
    else:
        answer = False

    print(answer)

solution("1234")