
def solution(my_string, letter):
    answer = ''

    for i in range(len(my_string)):
        if(my_string[i] == letter):
            continue
        else:
            answer += my_string[i]

    print(answer)

solution('abcdef','f')