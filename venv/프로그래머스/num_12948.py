
def solution(phone_number):
    # answer = ''

    # for i in phone_number:
    #     if(phone_number.index(i) < (len(phone_number) - 4)):
    #         answer += '*'
    #     else:
    #         answer += i

    r = len(phone_number) - 4
    answer = '*'*r + phone_number[-4:]

    print(answer)

solution("027778888")