
def solution(s):

    answer = True

    s = s.lower()

    p_c = 0
    y_c = 0
    for i in s:
        if (i == 'p'):
            p_c += 1
        elif (i == 'y'):
            y_c += 1

    if(p_c == y_c):
        answer = True
    elif(p_c != y_c):
        answer = False
    elif(p_c == 0 or y_c == 0):
        answer = True
    else:
        answer = False

    print(answer)

solution("Pyy")