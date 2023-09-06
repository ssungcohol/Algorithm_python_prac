
def solution(my_string):
    # answer = 0

    str = my_string.split()

    answer = int(str[0])
    for s in range(1,len(str),2):
        if str[s] == '+' :
            answer += int(str[s+1])
        else:
            answer -= int(str[s+1])


    print(answer)

solution("3 + 4")